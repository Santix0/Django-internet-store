from django import template
from django.db.models import Count, F

from product.models import Product

register = template.Library()


# function that return all product from db
@register.simple_tag()
def get_products():
    return Product.objects.all()


# TODO: create the function that will get product by his slug
@register.inclusion_tag('product/product.html')
def get_product_by_slug():
    product = Product.objects.annotate(cnt=Count('product', filter=F('news__is_stoke'))).filter()
    return {'product': product}
