import pkg_resources


default_app_config = "pinax.eventlog.apps.AppConfig"
__version__ = pkg_resources.get_distribution("pinax-eventlog").version
