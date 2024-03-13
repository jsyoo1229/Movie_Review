from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import LoginForm, SignUpForm
from django.urls import reverse_lazy

signup = CreateView.as_view(

    form_class = SignUpForm,
    success_url = reverse_lazy('movie_list'),  # 예: 홈 페이지 또는 로그인 후 페이지로 리다이렉트
    template_name = 'accounts/form.html'
)



login = LoginView.as_view(
    authentication_form = LoginForm,
)

logout = LogoutView.as_view(
    next_page = '/'
)

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')