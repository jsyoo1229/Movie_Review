from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import datetime
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DeleteView,
    UpdateView,
    DetailView,
    CreateView,
    TemplateView,
    View,
)
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import requests


class HomeView(TemplateView):
    template_name = "movies/index.html"  # 홈 화면 템플릿

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # TMDb API를 사용하여 현재 상영 중인 영화 목록을 가져옴
        now_playing_url = "https://api.themoviedb.org/3/movie/now_playing?api_key=07bda5bfc4cadba3cc328f798766739f&language=en-US&page=1"
        now_playing_response = requests.get(now_playing_url)

        print("Status code for now_playing: ", now_playing_response.status_code)

        now_playing_movies = now_playing_response.json()["results"]

        print("Now playing movies: ", now_playing_movies)

        # 장르 목록을 가져옴
        genres_url = "https://api.themoviedb.org/3/genre/movie/list?api_key=07bda5bfc4cadba3cc328f798766739f&language=en-US"
        genres_response = requests.get(genres_url)

        print("Status code for genres: ", genres_response.status_code)

        genres = genres_response.json()["genres"]
        genres_dict = {genre["id"]: genre["name"] for genre in genres}

        print("Genres dict: ", genres_dict)

        for movie in now_playing_movies:
            movie["genre_names"] = [
                genres_dict.get(genre_id, "Unknown Genre")
                for genre_id in movie["genre_ids"]
            ]

        context["now_playing_movies"] = (
            now_playing_movies  # API 응답에서 영화 목록 추출
        )
        context["genres_dict"] = genres_dict

        return context


class TheaterDetailView(View):
    def get(self, request, pk):
        api_key = "07bda5bfc4cadba3cc328f798766739f"
        url = (
            f"https://api.themoviedb.org/3/movie/{pk}?api_key={api_key}&language=en-US&append_to_response=videos,credits"
        )
        response = requests.get(url)
        movie = response.json()

        #연도
        release_year = datetime.strptime(movie['release_date'], "%Y-%m-%d").year

        #감독
        directors = [member['name'] for member in movie['credits']['crew'] if member['job'] == 'Director']

        # 상위 5명의 배우 정보
        cast = movie['credits']['cast'][:5]  

        # 예고편 영상 URL 구성 (YouTube 기준)
        trailers = [video for video in movie['videos']['results'] if video['site'] == 'YouTube']
        trailer_urls = [f"https://www.youtube.com/watch?v={video['key']}" for video in trailers]

        context = {
                'movie': movie,
                'directors': directors,
                'cast': cast,
                'trailers': trailer_urls,
                'release_year': release_year
            }

        return render(request, "movies/movie_detail.html", context)


theater_movie = TheaterDetailView.as_view()


class EOR_MovieListView(ListView):
    template_name = 'movies/EOR_movie_list.html'
    context_object_name = 'movies'
    

    def get_queryset(self):
        api_key = '07bda5bfc4cadba3cc328f798766739f'
        url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}&language=en-US&page=1'
        response = requests.get(url)
        return response.json().get('results', [])
    
    def get_queryset2(self):
            api_key = '07bda5bfc4cadba3cc328f798766739f'
            url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}&language=en-US&page=1'
            response = requests.get(url)
            movies = response.json().get('results', [])

            q = self.request.GET.get("q", "")
            if q:
                filtered_movies = [movie for movie in movies if q.lower() in movie['title'].lower()]
                return filtered_movies
            return movies
    
EOR_MovieList = EOR_MovieListView.as_view()    


class MovieListView(ListView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q", "")
        if q:
            qs = qs.filter(title__icontains=q)
        return qs


movie_list = MovieListView.as_view()


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("movie:movie_list")
    template_name = "movies/form.html"

    def form_valid(self, form):
        video = form.save(commit=False)  # commit=False는 DB에 저장하지 않고 객체만 반환
        video.author = self.request.user
        return super().form_valid(form)  # 이렇게 호출했을 때 저장합니다.


movie_create = MovieCreateView.as_view()


class MovieDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        return context

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        post = Post.objects.get(pk=pk)
        post.view_count += 1
        return super().get_object(queryset)


movie_detail = MovieDetailView.as_view()


class MovieUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("movie:movie_list")
    template_name = "movies/form.html"

    def test_func(self):
        return self.get_object().author == self.request.user


movie_update = MovieUpdateView.as_view()


class MovieDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("movie:movie_list")

    def test_func(self):
        return self.get_object().author == self.request.user


movie_delete = MovieDeleteView.as_view()


@login_required
def comment(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            return redirect("movie:movie_detail", pk)
    else:
        form = CommentForm()
    return render(
        request,
        "movies/form.html",
        {
            "form": form,
        },
    )


