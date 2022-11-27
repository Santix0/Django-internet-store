from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.urls import reverse_lazy


class User(AbstractUser):
    # groups = models.ForeignKey(Group, default='Buyer', on_delete=models.CASCADE)

    class Meta:
        db_table = 'auth_user'

    def get_absolute_url(self):
        return reverse_lazy('main_page')
