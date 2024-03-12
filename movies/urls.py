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
    path('<int:movie_id>/', views.MovieDetailView.as_view(), name='theater_movie_detail'),
    
    # path("tag/<str:tag>/", views.movie_tag, name="movie_tag"),
]