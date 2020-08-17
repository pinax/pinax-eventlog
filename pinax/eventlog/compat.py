"""
For Django < 3.1, rely on django-jsonfield-backport for JSONField
functionality

https://github.com/laymonage/django-jsonfield-backport#installation
https://github.com/laymonage/django-jsonfield-backport#why-create-another-one
"""

try:
    from django.db.models import JSONField  # noqa
except ImportError:
    from django_jsonfield_backport.models import JSONField  # noqa
