'Models representations on the admin panel'
from django.contrib import admin
from .models import (
    ShoppingCart, 
    CartItem
)

admin.site.register(ShoppingCart)
admin.site.register(CartItem)
