'''Models for Products app'''
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    '''Model for distributing products by categories'''
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("Product's category")
        verbose_name_plural = _("Product's categories")

    def __str__(self):
        return self.name

class Product(models.Model):
    'Product model'
    name = models.CharField(_('Name'), max_length=255, blank=False)
    description = models.TextField(_('Description'), )
    price = models.DecimalField(_('Price'), max_digits=5, decimal_places=2, blank=False)
    stock = models.IntegerField(_('Stock'), blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Category', related_name='products')
    created_at = models.TimeField(auto_now_add=True)


    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name


class Reviews(models.Model):
    '''Model for rating products'''
    user = models.ForeignKey(
        get_user_model(), 
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('User'),
        related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'), related_name='reviews')
    rating = models.IntegerField(
        _('Rating'),
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    comment = models.TextField(_('Comment'),  blank=True, null=True)
    created_at = models.TimeField(_('Create at'), auto_now_add=True)

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")