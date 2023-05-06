from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Username',
            'type': 'text'
        })),
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter Email',
            'type': 'email'
        })),
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter Password',
            'type': 'password'
        }))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'type': 'password'
        }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={
        'class' : 'px-24 py-3'
    }))
    password = forms.CharField( max_length=60, required=True, widget=forms.PasswordInput(attrs={
        'class' : 'px-24 py-3'
    }))