from django.contrib import admin
from django.contrib.sites.admin import SiteAdmin
from django.utils.translation import ugettext_lazy as _

from apps.core.sites import site

from .models import ProxySite, SiteProfile


class SiteProfileInline(admin.StackedInline):
    model = SiteProfile

    verbose_name_plural = _('profile')
    can_delete = False


@admin.register(ProxySite, site=site)
class ProxySiteAdmin(SiteAdmin):
    inlines = [
        SiteProfileInline,
    ]
