from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

class MovieListView(ListView):
    model = Post

    def get_queryset(self):
        qs = super().get_quertset()
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs       
        

movie_list = MovieListView.as_view()


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('movie:post_list')
    template_name = 'movie/form.html'


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
    success_url = reverse_lazy('movie:post_list')
    template_name = 'movie/form.html'

    def test_func(self):
        return self.get_object().author == self.request.user    


movie_update = MovieUpdateView.as_view()


class MovieDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('movie:post_list')

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
            comment.authot = request.user
            comment.save()

            return redirect('movie: movie_detail', pk)
    else:
        form = CommentForm()        
    return render(request, 'movie/form.html', {
        'form': form,
    })       

