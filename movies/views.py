from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView, TemplateView, View
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import requests



class HomeView(TemplateView):
    template_name = 'movies/index.html'  # 홈 화면 템플릿

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # TMDb API를 사용하여 현재 상영 중인 영화 목록을 가져옴
        now_playing_url = "https://api.themoviedb.org/3/movie/now_playing?api_key=07bda5bfc4cadba3cc328f798766739f&language=en-US&page=1"
        now_playing_response = requests.get(now_playing_url)

        print("Status code for now_playing: ", now_playing_response.status_code)  

        now_playing_movies = now_playing_response.json()['results']

        print("Now playing movies: ", now_playing_movies) 


        # 장르 목록을 가져옴
        genres_url = "https://api.themoviedb.org/3/genre/movie/list?api_key=07bda5bfc4cadba3cc328f798766739f&language=en-US"
        genres_response = requests.get(genres_url)

        print("Status code for genres: ", genres_response.status_code)

        genres = genres_response.json()['genres']
        genres_dict = {genre['id']: genre['name'] for genre in genres}

        print("Genres dict: ", genres_dict)

        for movie in now_playing_movies:
            movie['genre_names'] = [genres_dict.get(genre_id, "Unknown Genre") for genre_id in movie['genre_ids']]

        context['now_playing_movies'] = now_playing_movies  # API 응답에서 영화 목록 추출
        context['genres_dict'] = genres_dict

        return context
    

class MovieDetailView(View):
    def get(self, request, movie_id):
        api_key = '07bda5bfc4cadba3cc328f798766739f'
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
        response = requests.get(url)
        movie = response.json()

        return render(request, 'movies/movie_detail.html', {'movie': movie})    


class MovieListView(ListView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs       
        

movie_list = MovieListView.as_view()


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('movie:movie_list')
    template_name = 'movies/form.html'


    def form_valid(self, form):
        video = form.save(commit=False) # commit=False는 DB에 저장하지 않고 객체만 반환
        video.author = self.request.user
        return super().form_valid(form) # 이렇게 호출했을 때 저장합니다.



movie_create = MovieCreateView.as_view()


class MovieDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
    
    def get_object(self, queryset = None):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk = pk)
        post.view_count += 1
        return super().get_object(queryset)

movie_detail = MovieDetailView.as_view()


class MovieUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('movie:movie_list')
    template_name = 'movies/form.html'

    def test_func(self):
        return self.get_object().author == self.request.user    


movie_update = MovieUpdateView.as_view()


class MovieDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('movie:movie_list')

    def test_func(self):
        return self.get_object().author == self.request.user


movie_delete = MovieDeleteView.as_view()

@login_required
def comment(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            return redirect('movie:movie_detail', pk)
    else:
        form = CommentForm()        
    return render(request, 'movies/form.html', {
        'form': form,
    })       






# import requests  # requests 라이브러리를 가져와, HTTP 요청을 보낼 수 있게 해줍니다.

# from .models import Movie  # 현재 앱의 models.py에서 Movie 모델을 가져옵니다.

# def fetch_and_store_movies():  # 현재 상영 중인 영화 데이터를 가져와 저장하는 함수입니다.
#     url = "https://api.themoviedb.org/3/movie/now_playing?api_key=YOUR_API_KEY&language=en-US&page=1"  # TMDb API로부터 현재 상영 중인 영화 목록을 가져오는 URL입니다. 여기서 YOUR_API_KEY 부분을 실제 키로 바꿔야 합니다.
    
#     response = requests.get(url)  # 위 URL로 HTTP GET 요청을 보내고, 응답을 response 변수에 저장합니다.
#     data = response.json()  # 응답 데이터를 JSON 형식으로 파싱합니다.

#     for item in data['results']:  # 응답 데이터 중 영화 목록을 순회합니다.
#         movie = Movie(  # 각 영화 정보를 이용해 Movie 모델 인스턴스를 생성합니다.
#             title=item['title'],  # 영화 제목
#             genre=",".join([str(genre_id) for genre_id in item['genre_ids']]),  # 장르 ID를 문자열로 변환하여 저장합니다. 실제 사용 시 장르 이름으로 변환하는 것이 좋습니다.
#             is_showing=True,  # 현재 상영 중임을 나타냅니다.
#             image_url=f"https://image.tmdb.org/t/p/w500{item['poster_path']}",  # 영화 포스터 이미지 URL
#             rating=item['vote_average']  # 영화 평점
#         )
#         movie.save()  # 생성한 Movie 인스턴스를 데이터베이스에 저장합니다.
