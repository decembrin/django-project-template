from django.contrib.admin.sites import AdminSite as BaseAdminSite
from django.utils.translation import gettext_lazy


class AdminSite(BaseAdminSite):
    # Text to put at the end of each page's <title>.
    site_title = gettext_lazy('Django site admin')

    # Text to put in each page's <h1>.
    site_header = gettext_lazy('Django administration')

    # Text to put at the top of the admin index page.
    index_title = gettext_lazy('Site administration')


site = AdminSite()
