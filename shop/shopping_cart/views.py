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
# class Cart(ListView):
#     model = Order
#     context_object_name = 'cart'
#     template_name = 'shopping_cart/shopping_cart.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
#
#     def get_queryset(self):
#         return Order.objects.filter(is_ordered=True)


# function that give to user's cart the products that he added in cart
@login_required()
def cart_products(request, user_id) -> dict:
    # creating object of Order model with specific arguments
    cart = Order.objects.filter(is_ordered=True, owner_id=user_id)
    # creating car for sum total price of user's cart
    total_price = 0
    for items in cart.all():
        for item in items.items.all():
            total_price += item.product.price
    # creating context
    context = {
        'cart': cart,
        'total_price': total_price,
    }

    return render(request, 'shopping_cart/shopping_cart.html', context)


# Function that add the products from main page to user's page
@login_required()
def add_to_cart(request, user_id: int, item_id: int):
    # filter the product by id
    product_to_add = Product.objects.filter(pk=item_id)
    # check if product exists
    if product_to_add.exists():
        # creating object of product for cart
        cart_item = OrderItem.objects.create(product_id=item_id, is_ordered=True)
        cart = Order.objects.create(owner=request.user, is_ordered=True)
        cart.save()
        cart.items.add(cart_item)
    return redirect('main_page')


@login_required()
def delete_from_cart(request, user_id: int, item_id: int):
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
def total_price_of_cart(request, owner_id: int) -> dict:
    order_items = Order.objects.filter(is_ordered=True, owner_id=owner_id)
    total_price = 0
    for items in order_items.all():
        for item in items.items.all():
            total_price += item.product.price

    context = {
        'order_items': order_items,
        'total_price': total_price,
    }

    return render(request, 'shopping_cart/cart_total_cost.html', context)
