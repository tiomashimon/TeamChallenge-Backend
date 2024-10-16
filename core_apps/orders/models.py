from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from core_apps.products.models import Product


class OrderStatus(models.Model):
    '''Status for Order model'''
    name = models.CharField(_('Name'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Order(models.Model):
    '''Order model for placing orders'''
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_('User'),
        related_name='orders'
    )
    status = models.ForeignKey(
        OrderStatus,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('Status'),
        related_name='orders'
    )
    total_price = models.DecimalField(
        _('Total Price'),
        max_digits=10,  
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    def __str__(self):
        return f'Order #{self.id} by {self.user}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderStatusHistory(models.Model):
    '''History for orders'''
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name=_('Order'),
        related_name='history_of_statuses'
    )
    status = models.ForeignKey(
        OrderStatus,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('Status'),
        related_name='history_of_statuses'
    )
    changed_at = models.DateTimeField(_('Changed at'), auto_now_add=True)

    def __str__(self):
        return f'Status {self.status} for Order #{self.order.id}'

    class Meta:
        verbose_name = 'Order Status History'
        verbose_name_plural = 'Order Status Histories'


class OrderItem(models.Model):
    '''Items in a new Order'''
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name=_('Order'),
        related_name='items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('Product'),
        related_name='ordered_items'
    )
    quantity = models.IntegerField(_('Quantity'), validators=[MinValueValidator(1)])
    price = models.DecimalField(
        _('Price'),
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    def __str__(self):
        return f'{self.quantity} x {self.product.name} for Order #{self.order.id}'

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
