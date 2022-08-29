from django.urls import path

from .views import *
from .models import *


urlpatterns = [
    path('', Cart.as_view(), name='user_cart'),
    path(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name='add_to_cart'),
    path('cart_total_cost', Order.get_cart_total_cost, name='cart_total_cost')
]
