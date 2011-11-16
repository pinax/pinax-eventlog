from datetime import datetime

from django.conf import settings
from django.db import models

from django.contrib.auth.models import User

from jsonfield.fields import JSONField


PUSHER_CONFIG = getattr(settings, "PUSHER_CONFIG", None)


class Log(models.Model):
    
    user = models.ForeignKey(User, null=True)
    timestamp = models.DateTimeField(default=datetime.now)
    action = models.CharField(max_length=50)
    extra = JSONField(default="{}")
    
    class Meta:
        ordering = ["-timestamp"]


def log(user, action, extra):
    if (user is not None and not user.is_authenticated()):
        user = None
    
    if PUSHER_CONFIG:
        import pusher
        p = pusher.Pusher(
            app_id=PUSHER_CONFIG["app_id"],
            key=PUSHER_CONFIG["key"],
            secret=PUSHER_CONFIG["secret"]
        )
        # send utc date (http://stackoverflow.com/questions/948532/how-do-you-convert-a-javascript-date-to-utc/951417#951417)
        p["event_log"].trigger(action, {
            "user": user.username,
            "extra": extra,
            "date": datetime.utcnow().isoformat()
        })
    
    return Log.objects.create(user=user, action=action, extra=extra)
