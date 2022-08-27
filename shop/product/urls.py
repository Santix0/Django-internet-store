from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPageProducts.as_view(), name='main_page'),
    path('<str:slug>', ShowAloneProduct.as_view(), name='product'),
    path('add_product/', AddProductView.as_view(), name='add_product'),
]
