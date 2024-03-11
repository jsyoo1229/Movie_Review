from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Add a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", required=True, widget=forms.TextInput(attrs={'placeholder': 'Hugh Jackman', 'pattern': '^[a-zA-Z][a-zA-Z0-9-_\.]{8,20}$'}))
    password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput(attrs={'placeholder': '******', 'pattern': '(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'}))    
