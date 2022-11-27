from django.contrib.auth.forms import forms, UserCreationForm
from django.contrib.auth.forms import UserChangeForm

from .models import *


class UserUpdateForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))

    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}))

    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}))

    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']


class PasswordChange(UserChangeForm):
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your password'}))

    class Meta:
        model = User
        fields = ['password']


class UserSignUpForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'placeholder': 'Enter username'
    }))
    email = forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={
        'placeholder': 'Enter email'
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password'
    }))
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password again'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1',
                  'password2',
                  )
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter name'}),
        }


class UserSignInForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'placeholder': 'Enter username'
    }))
    password = forms.IntegerField(label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter name'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter name'})
        }
