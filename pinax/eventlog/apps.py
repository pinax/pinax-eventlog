import importlib

from django.apps import AppConfig as BaseAppConfig
from django.utils.translation import ugettext_lazy as _


class AppConfig(BaseAppConfig):

    name = "pinax.eventlog"
    label = "pinax_eventlog"
    verbose_name = _("Pinax Eventlog")
