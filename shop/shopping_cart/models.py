from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy

from product.models import Product


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    data_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner}'

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total_cost(self):
        return sum([item.product.price for item in self.items.all()])

    def get_absolute_url(self):
        return reverse_lazy('shopping_cart', kwargs={'pk': self.pk})
