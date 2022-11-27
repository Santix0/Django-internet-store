import random

import requests
from django.contrib.auth.decorators import login_required
from django.contrib.messages.context_processors import messages

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate

from .forms import AddProduct
from .models import *
from bs4 import BeautifulSoup


# Show all products on main page
class MainPageProducts(ListView):
    model = Product
    # paginate_by = 1
    context_object_name = 'product'
    template_name = 'product/main_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['name'] = Product.objects.get(pk=self.kwargs['id'])
        return context

    def get_queryset(self):
        return Product.objects.order_by('-created_at')


# function that show to user product separately that is filtered by slug
def get_product_separately(request, slug: str) -> dict:
    # get product by slug
    product = Product.objects.get(slug=slug)

    context = {'product': product}

    return render(request, 'product/product.html', context)


# Class for add product from user to db
class AddProductView(CreateView):
    form_class = AddProduct
    template_name = 'product/adding_product.html'
    success_url = reverse_lazy('main_page')


# The form for adding product by person to db
@login_required()
def adding_product(request) -> dict:
    # checking the method of request
    if request.method == 'POST':
        # creating object for adding to db
        form = AddProduct(request.POST)
        form.add()
        if form.is_valid():
            form.save()
            return redirect('main_page')
        else:
            form = AddProduct()
    context = {'form': form}
    return render(request, 'product/adding_product.html', context)


def searching_system(request) -> dict:
    query = request.GET.get('search', '')
    searched_products = Product.objects.filter(
        Q(name__icontains=query)
    )
    # creating context
    context = {
        'searched_products': searched_products,
    }

    return render(request, 'product/searching_system.html', context)


# function that filter product by category
def get_categorys_product(request, category_id: int) -> dict:
    # filter product by id with using Q object
    product_to_site = Product.objects.filter(
        category_id=category_id
    )
    # creating context
    context = {
        'products': product_to_site
    }

    return render(request, 'product/products_filtered_by_category_id.html', context)


# function that return all categories
def get_catalog(request) -> dict:
    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'product/catalog.html', context)

