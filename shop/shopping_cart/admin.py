from django.contrib import admin
from .models import Order, OrderItem, Checkout


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'is_ordered',
                    'date_added', 'data_ordered'
                    )
    list_filter = ('product', 'is_ordered',
                    )
    search_fields = ('product',)
    list_display_links = ('product',)
    readonly_fields = ('date_added', 'data_ordered',)


admin.site.register(Checkout)
admin.site.register(Order)
admin.site.register(OrderItem, OrderItemAdmin)
