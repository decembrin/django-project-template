from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

from apps.core.sites import site

from .models import ProxyGroup, User


@admin.register(ProxyGroup, site=site)
class ProxyGroupAdmin(BaseGroupAdmin):
    pass


@admin.register(User, site=site)
class UserAdmin(BaseUserAdmin):
    search_fields = ('first_name', 'last_name', 'email')
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
            )
        }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name')
        }),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            )
        }),
        (_('Important dates'), {
            'fields': (
                'last_login',
                'date_joined'
            )
        }),
    )
    ordering = ('email', )
