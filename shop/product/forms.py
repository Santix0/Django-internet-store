from django import forms
# from django.product.exceptions import ValidationError
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
