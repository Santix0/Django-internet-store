from django.urls import path

from .views import *
from .models import *

urlpatterns = [
    path('', cart_products, name='user_cart'),
    # path(r'^add-to-cart/(?P<item_slug>[-\w]+)/$', add_to_cart, name='add_to_cart'),
    path('<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('checkout/<str:user_name>', checkout, name='checkout'),
    path('delete_from_cart/<int:item_id>/', delete_from_cart, name='delete_from_cart'),
    path('order/', order, name='order'),
    path('order/delete_from_order/<int:order_id>/', delete_order, name='delete_order')
]
