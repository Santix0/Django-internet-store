from django.urls import path

from .views import *

urlpatterns = [
    path('user_data/<int:user_id>/', user_data, name='user_data'),
    path('user_change_account/<int:user_id>', ChangeUserAccount.as_view(), name='change_user_account'),
    path('user_change_password/<int:user_id>', PasswordChange.as_view(), name='change_password'),
    path('sign_up/', sign_up, name='sign_up'),
    path('sing_in/', sign_in, name='sign_in'),
    path('logout/', logout_user, name='logout_user'),
]
