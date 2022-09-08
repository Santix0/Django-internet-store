from django.urls import path

from .views import *
from .models import *

urlpatterns = [
    path('', Cart.as_view(), name='user_cart'),
    # path(r'^add-to-cart/(?P<item_slug>[-\w]+)/$', add_to_cart, name='add_to_cart'),
    path('<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('cart_total_cost', Order.get_cart_total_cost, name='cart_total_cost'),
    path('delete_from_cart/<int:item_id>/', delete_form_cart, name='delete_from_cart')
    # path('', add_to_cart)
]
