from django import template
from django.db.models import Count, F

from product.models import Product, Category

register = template.Library()


# function that return all products from db
@register.simple_tag()
def get_products():
    return Product.objects.all()


@register.simple_tag()
def get_all_categories():
    return Category.objects.all()
