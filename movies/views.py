from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


class MovieListView(ListView):
    model = Post

movie_list = MovieListView.as_view()


class MovieCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('movie:post_list')
    template_name = 'movie/form.html'

movie_create = MovieCreateView.as_view()


class MovieDetailView(DetailView):
    model = Post

movie_detail = MovieDetailView.as_view()


class MovieUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('movie:post_list')
    template_name = 'movie/form.html'

movie_update = MovieUpdateView.as_view()


class MovieDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('movie:post_list')

movie_delete = MovieDeleteView.as_view()