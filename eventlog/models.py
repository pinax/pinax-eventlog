from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone

import jsonfield

from .signals import event_logged


class Log(models.Model):

    user = models.ForeignKey(
        getattr(settings, "AUTH_USER_MODEL", "auth.User"),
        null=True,
        on_delete=models.SET_NULL
    )
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
    action = models.CharField(max_length=50, db_index=True)
    extra = jsonfield.JSONField()

    class Meta:
        ordering = ["-timestamp"]


def log(user, action, extra=None):
    if (user is not None and not user.is_authenticated()):
        user = None
    if extra is None:
        extra = {}
    event = Log.objects.create(user=user, action=action, extra=extra)
    event_logged.send(sender=Log, event=event)
    return event
