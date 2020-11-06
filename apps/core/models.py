from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProxySite(Site):
    class Meta(object):
        proxy = True
        verbose_name = _('site')
        verbose_name_plural = _('sites')


class SiteProfile(models.Model):
    extra_head = models.TextField(blank=True, default='')
    site = models.OneToOneField('sites.Site', on_delete=models.CASCADE,
                                related_name='profile')

    class Meta(object):
        verbose_name = _('profile')
