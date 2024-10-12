'''Models for Products app'''
from django.db import models
from django.utils.translation import gettext_lazy as _



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
