from django.db import models
from django.urls import reverse_lazy

from product.models import Product
from useraccount.models import User

from django_countries.fields import CountryField


class OrderItem(models.Model):
    id = models.BigAutoField(unique=True, primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    data_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    id = models.BigAutoField(unique=True, primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.items}'

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total_cost(self):
        return sum([item.product.price for item in self.items.all()])

    def get_absolute_url(self):
        return reverse_lazy('shopping_cart', kwargs={'pk': self.pk})


class Checkout(models.Model):
    full_name = models.CharField(max_length=100)
    user_id = models.ManyToManyField(User, blank=True, null=True)
    address = models.CharField(max_length=100)
    zip = models.CharField(max_length=50)
    country = CountryField(multiple=False)
    phone = models.CharField(max_length=50)
    products = models.ManyToManyField(Order)

    def __str__(self):
        return f'{self.full_name}'
