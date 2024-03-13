from django.urls import path
from . import views

app_name = 'movie'


urlpatterns = [
    path("", views.movie_list, name="movie_list"),
    path("<int:pk>/", views.movie_detail, name="movie_detail"),
    path("create/", views.movie_create, name="movie_create"),
    path("<int:pk>/update/", views.movie_update, name="movie_update"),
    path("<int:pk>/delete/", views.movie_delete, name="movie_delete"),
    path('comments/<int:pk>/', views.comment, name='comment_create'),
    path('theater/<int:pk>/', views.theater_movie, name='theater_movie_detail'), 
    path('end_of_release_movies/', views.EOR_MovieList, name='EOR_MovieList'),
]