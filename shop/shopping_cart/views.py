from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.db import models

from .models import Order, OrderItem

# this class return user of store his products in cart
from product.models import Product

from .utils import generate_order_id


# create class that will return all products in cart
class Cart(ListView):
    model = Order
    context_object_name = 'cart'
    template_name = 'shopping_cart/shopping_cart.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Order.objects.filter(is_ordered=True)


# decorator for check if user is auth
# TODO: figure out how with django orm create ManyToManyField for Order object
@login_required()
def add_to_cart(request, item_id):
    # filter the product by id
    product_to_add = Product.objects.filter(pk=item_id)
    # check if product exists
    if product_to_add.exists():
        # creating object of product for cart
        cart_item = OrderItem.objects.create(product_id=item_id, is_ordered=True)
        cart = Order.objects.create(owner=request.user, is_ordered=True)
        cart.save()
        cart.items.add(cart_item)
        # messages.info(request, 'Product added to cart')
    return redirect('main_page')


@login_required()
def delete_form_cart(request, item_id):
    # filter the product from cart by pk
    product_to_delete = Order.objects.filter(pk=item_id)
    # check if product exists
    if product_to_delete.exists():
        # delete the product cart
        product_to_delete.delete()
    return redirect('main_page')


# TODO: figure out how do this function
# return total cost of cart
@login_required()
def total_cost(request):
    pass
