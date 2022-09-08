from django import template

from product.models import Product

from shopping_cart.models import OrderItem, Order

register = template.Library()
