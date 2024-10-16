'''Model representation on Admin Panel'''
from django.contrib import admin
from .models import (
    Order,
    OrderItem,
    OrderStatus,
    OrderStatusHistory
)


admin.site.register(Order)
admin.site.register(OrderStatusHistory)
admin.site.register(OrderItem)
admin.site.register(OrderStatus)