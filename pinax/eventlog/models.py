from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils import timezone

from .compat import JSONField
from .signals import event_logged


class Log(models.Model):

    user = models.ForeignKey(
        getattr(settings, "AUTH_USER_MODEL", "auth.User"),
        null=True,
        on_delete=models.SET_NULL
    )
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
    action = models.CharField(max_length=50, db_index=True)
    content_type = models.ForeignKey(ContentType, null=True, on_delete=models.SET_NULL, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    obj = GenericForeignKey("content_type", "object_id")
    extra = JSONField(encoder=DjangoJSONEncoder, blank=True)

    @property
    def template_fragment_name(self):
        return f"pinax/eventlog/{self.action.lower()}.html"

    class Meta:
        ordering = ["-timestamp"]


def log(user, action, extra=None, obj=None, dateof=None):
    if (user is not None and not user.is_authenticated):
        user = None
    if extra is None:
        extra = {}
    content_type = None
    object_id = None
    if obj is not None:
        content_type = ContentType.objects.get_for_model(obj)
        object_id = obj.pk
    if dateof is None:
        dateof = timezone.now()

    event = Log.objects.create(
        user=user,
        action=action,
        extra=extra,
        content_type=content_type,
        object_id=object_id,
        timestamp=dateof
    )
    event_logged.send(sender=Log, event=event)
    return event
