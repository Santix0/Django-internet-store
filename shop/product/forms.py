from django import forms
# from django.product.exceptions import ValidationError
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Category, Product


# form for adding product by user(only if he's register)
class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'slug', 'price', 'description', 'category']
        # do custom settings for input fields
        widgets = {
            'name': forms.TextInput(),
            'slug': forms.TextInput(),
            'price': forms.NumberInput(),
            'description': forms.TextInput(),
            'category': forms.Select(),
        }

#
# class UserSignUpForm(UserCreationForm):
#     username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
#         'placeholder': 'Enter username'
#     }))
#     email = forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={
#         'placeholder': 'Enter email'
#     }))
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
#         'placeholder': 'Enter password'
#     }))
#     password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
#         'placeholder': 'Enter password again'
#     }))
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1',
#                   'password2',
#                   )
#         widgets = {
#             'username': forms.TextInput(attrs={'placeholder': 'Enter name'}),
#         }


# class UserSignInForm(forms.ModelForm):
#     username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
#         'placeholder': 'Enter username'
#     }))
#     password = forms.IntegerField(label='Password', widget=forms.PasswordInput(attrs={
#         'placeholder': 'Enter Password'
#     }))
#
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#         widgets = {
#             'username': forms.TextInput(attrs={'placeholder': 'Enter name'}),
#             'password': forms.PasswordInput(attrs={'placeholder': 'Enter name'})
#         }
