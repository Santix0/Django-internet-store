from django.urls import path

from .views import *


urlpatterns = [
    path('', Cart.as_view(), name='user_cart'),
    path(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name='add_to_cart'),
]
