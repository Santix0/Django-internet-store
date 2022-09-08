from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPageProducts.as_view(), name='main_page'),
    path('<str:slug>', get_product_separately, name='product'),
    path('add_product/', AddProductView.as_view(), name='add_product'),
    path('<str:product_name>', searching_system, name='searching_system'),
]
