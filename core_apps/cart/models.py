'''Database models for cart app'''
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from core_apps.products.models import Product


class ShoppingCart(models.Model):
    '''Shopping cart for User'''

    def __str__(self):
        return f'Shopping cart of {self.user.username}'
    
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_('User'),
        related_name='shopping_cart',  
    )   
    created_at = models.TimeField(_('Created at'), auto_now_add=True)

   
    class Meta:
        verbose_name = _("Shopping Cart")
        verbose_name_plural = _("Shopping Carts")


class CartItem(models.Model):
    '''Cart item for Shopping cart'''

    def __str__(self):
        return f"{self.cart.user.username}'s Cart item"
    
    cart = models.ForeignKey(
        ShoppingCart,
        on_delete=models.CASCADE,
        verbose_name=_('Cart Items'),
        related_name='cart_items',  
    )   
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Product'),
        related_name='product_in_cart',
    )

    class Meta:
        verbose_name = _("Cart item")
        verbose_name_plural = _("Cart items")