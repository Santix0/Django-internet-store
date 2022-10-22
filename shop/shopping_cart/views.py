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

from .forms import CheckoutForm
from .models import Order, OrderItem, Checkout

# this class return user of store his products in cart
from product.models import Product

from .utils import generate_order_id


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
# @login_required()
# def add_to_cart(request, user_id: int, item_id: int):
#     # filter the product by id
#     product_to_add = Product.objects.filter(pk=item_id)
#     # check if product exists
#     if product_to_add.exists():
#         cart = Order.objects.filter(owner_id=request.user.id)
#         # checking if cart objects with specific user_id exists
#         if cart.exists():
#             # creating objects of OrderItem to add item to order
#             cart_item = OrderItem.objects.create(product_id=item_id, is_ordered=True)
#             cart.items.add(cart_item)
#         else:
#             # creating object of OrderItem for cart
#             cart_item = OrderItem.objects.create(product_id=item_id, is_ordered=True)
#             cart = Order.objects.create(owner=request.user, is_ordered=True)
#             cart.save()
#             cart.items.add(cart_item)
#     return redirect('main_page')


@login_required()
def delete_from_cart(request, user_id: int, item_id: int):
    # filter the product from cart by pk
    product_to_delete = Order.objects.filter(pk=item_id)
    # check if product exists
    if product_to_delete.exists():
        # delete the product cart
        product_to_delete.delete()
    return redirect('main_page')


# return total cost of cart
@login_required()
def total_price_of_cart(request, owner_id: int) -> dict:
    order_items = Order.objects.filter(is_ordered=True, owner_id=owner_id)
    total_price = 0
    # going through items in cart for get the price of each product
    for items in order_items.all():
        for item in items.items.all():
            # adding each product's price to total price
            total_price += item.product.price

    context = {
        'order_items': order_items,
        'total_price': total_price,
    }

    return render(request, 'shopping_cart/checkout.html', context)


@login_required()
def checkout(request, user_id: int, user_name: str) -> dict:
    if request.method == 'POST':
        # creating form
        form = CheckoutForm(request.POST)
        # creating attributes for order object
        full_name = request.POST['full_name']
        address = request.POST['address']
        zip = request.POST['zip']
        country = request.POST['country']
        phone = request.POST['phone']
        products = Order.objects.filter(owner_id=request.user.id)
        # create order object
        order = Checkout.objects.create(full_name=full_name, address=address,
                                        zip=zip, country=country, phone=phone,
                                        )
        # adding user_id to checkout object
        order.user_id.set(f"{user_id}")
        # adding products to checkout object
        for product in products:
            order.products.add(product)
        return redirect('main_page')
    else:
        form = CheckoutForm()

    context = {
        'form': form,
    }

    return render(request, 'shopping_cart/checkout.html', context)


@login_required()
def order(request, user_id: int) -> dict:
    products = Checkout.objects.filter(user_id=user_id)

    context = {
        'products': products,
    }

    return render(request, 'shopping_cart/order.html', context)
