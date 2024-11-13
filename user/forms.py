from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.forms.widgets import Input, PasswordInput

# from user.models import User


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            "username": Input(attrs={
                'id': 'username',
                'class': 'form-control',
                'type': 'text',
                'name': 'username',
                'placeholder': 'Username',
            }),
            "password": Input(attrs={
                'id': 'password',
                'class': 'form-control',
                'type': 'password',
                'name': 'password',
                'placeholder': 'Password',
            })
        }


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Password',}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        widgets = {
            "username": Input(attrs={
                'id': 'username',
                'class': 'form-control',
                'type': 'text',
                'name': 'username',
                'placeholder': 'Username',
            }),
            "password1": PasswordInput(attrs={
                'id': 'password1',
                'type': 'password',
                'name': 'password1',
            }),
            "password2": PasswordInput(attrs={
                'id': 'password2',
                'type': 'password',
                'name': 'password2',
            })
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
