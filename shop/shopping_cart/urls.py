from django.urls import path

from .views import *
from .models import *
from product.views import searching_system

urlpatterns = [
    path('', cart_products, name='user_cart'),
    # path(r'^add-to-cart/(?P<item_slug>[-\w]+)/$', add_to_cart, name='add_to_cart'),
    path('<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('total_cost', total_price_of_cart, name='checkout'),
    path('delete_from_cart/<int:item_id>/', delete_from_cart, name='delete_from_cart'),
    # path('result/<str:product_name>', searching_system, name='searching_product'),
]
