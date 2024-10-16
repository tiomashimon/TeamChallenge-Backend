from django.contrib import admin
from .models import (
    Product, 
    Category,
    Reviews
)

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Reviews)