from django.conf import settings
from django.db import models
from django.utils import timezone

from django.contrib.contenttypes.models import ContentType

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
    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    extra = jsonfield.JSONField()

    @property
    def template_fragment_name(self):
        return "eventlog/{}.html".format(self.action.lower())

    class Meta:
        ordering = ["-timestamp"]


def log(user, action, extra=None, obj=None):
    if (user is not None and not user.is_authenticated()):
        user = None
    if extra is None:
        extra = {}
    content_type = None
    object_id = None
    if obj is not None:
        content_type = ContentType.objects.get_for_model(obj)
        object_id = obj.pk
    event = Log.objects.create(
        user=user,
        action=action,
        extra=extra,
        content_type=content_type,
        object_id=object_id
    )
    event_logged.send(sender=Log, event=event)
    return event
