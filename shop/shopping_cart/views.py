from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

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


# decorator for checking if user is auth
@login_required()
def add_to_cart(request, *product_pk):
    # filter the product by pk
    product_to_add = Product.objects.filter(pk=product_pk)
    if product_to_add.exists():
        # creating object of product for cart
        cart = Cart.objects.create(owner=product_to_add.created_by, items=product_to_add,
                                   is_ordered=True)
        cart.save()
        messages.info(request, 'Product added to cart')
    return redirect('main_page')
