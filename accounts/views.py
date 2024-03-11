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


    # initial = {}
    # template_name = 'accounts/form.html'

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(initial=self.initial)
    #     return render(request, self.template_name, {'form': form})

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)
    #         return redirect('movie_list')  # 예: 홈 페이지 또는 로그인 후 페이지로 리다이렉트
    #     return render(request, self.template_name, {'form': form})
)



login = LoginView.as_view(
    authentication_form = LoginForm,
    template_name = 'accounts/form.html',
)

logout = LogoutView.as_view(
    next_page = '/accounts/login/'
)

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')