from django.db import models
from django.contrib.auth.models import User

# 장르 모델
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 영화 모델
class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name='movies')  # 다대다 관계
    
    def __str__(self):
        return self.title

    
# 게시물 모델
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  # 1대다 관계
    title = models.CharField(max_length=200)
    content = models.TextField()
    thumb_image = models.ImageField(
        upload_to='movies/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(
        upload_to='movies/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title    

    def get_absolute_url(self):
        return f'/tube/{self.pk}/'
    
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.message    
    




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()  # 사용자가 입력한 이름
    email = models.EmailField(blank=True, null=True)  # 사용자 이메일
    website = models.URLField(blank=True, null=True)  # 사용자 웹사이트
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.message
