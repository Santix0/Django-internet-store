from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at',
                    'updated_at', 'category'
                    )
    list_filter = ('name', 'slug', 'category',
                   'created_at')
    search_fields = ('name', 'slug')
    list_display_links = ('name', 'slug')
    readonly_fields = ('created_at', 'updated_at')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title', 'slug')
    search_fields = ('title', 'slug')
    list_display_links = ('title', 'slug')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

