from django import template

from product.models import Product

register = template.Library()


@register.simple_tag
def get_item_price(*item_pk: int) -> int:
    return Product.objects.get(pk=item_pk)
