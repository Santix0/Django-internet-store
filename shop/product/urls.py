from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPageProducts.as_view(), name='main_page'),
    path('product_separately/<str:slug>', get_product_separately, name='product'),
    path('add_product/', AddProductView.as_view(), name='add_product'),
    path('searching_system/', searching_system, name='searching_system'),
    path('catalog/all', get_catalog, name='catalog'),
    path('catalog/all/<int:category_id>', get_categorys_product, name='get_categorys_product'),
    # path('user/sign_up/', sign_up, name='sign_up'),
    # path('user/sing_in/', sign_in, name='sign_in'),
    # path('user/logout/', logout_user, name='logout_user'),
]
