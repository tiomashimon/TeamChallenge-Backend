from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import (
    User,
    Role
    )

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'username', 'role', 'is_active', 'is_staff', 'last_login']
    search_fields = ['email', 'username']
    list_filter = ['is_active', 'is_staff', 'is_superuser', 'role']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('username',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'role')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'role', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )
    readonly_fields = ['last_login']


admin.site.register(User, UserAdmin)
admin.site.register(Role)