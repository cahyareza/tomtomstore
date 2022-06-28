# myproject/apps/magazine/apps.py
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class WebpageAppConfig(AppConfig):
    name = "myproject.apps.webpage"
    verbose_name = _("Webpage")