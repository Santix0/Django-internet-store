import requests

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.db.models import Q

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


# function that show to user product that is filtered by slug
def get_product_separately(request, slug):
    # get product by slug
    product = Product.objects.get(slug=slug)

    context = {'product': product}

    return render(request, 'product/product.html', context)


# Class for add product from person to db
class AddProductView(CreateView):
    form_class = AddProduct
    template_name = 'product/adding_product.html'
    success_url = reverse_lazy('main_page')


# The form for adding product by person to data base
def adding_product(request):
    if request.method == 'POST':
        form = AddProduct(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
        else:
            form = AddProduct()
    context = {'form': form}
    return render(request, 'product/adding_product.html', context)


# TODO: create function that will make the search field
def searching_system(request):
    searching_product = requests.GET.get()
    if searching_product:
        product = Product.objects.filter(
            Q(name__icontains=searching_product) & Q(category__icontains=searching_product))
        return product
    else:
        # If not the searched, return default product

        product = Product.objects.all().ordered_by('-created_at')
        return product
