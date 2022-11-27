from django.db import models
from django.urls import reverse, reverse_lazy

from .utils import validation_if_number_is_positive

from useraccount.models import User


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    id = models.BigAutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validation_if_number_is_positive])
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator', default=1)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, max_length=150, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('product', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-created_at', 'name')
