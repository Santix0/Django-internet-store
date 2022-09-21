from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPageProducts.as_view(), name='main_page'),
    path('product_separately/<str:slug>', get_product_separately, name='product'),
    path('add_product/', AddProductView.as_view(), name='add_product'),
    # path('<str:product_name>/', searching_system, name='searching_system'),
    # path('?catalog=<int:category_id>/', get_categorys_product, name='category_product'),
    path('add_product/<str:product_name>', searching_system, name='add_to_product_searching_system')
]
