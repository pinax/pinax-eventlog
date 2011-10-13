from datetime import datetime

from django.db import models

from django.contrib.auth.models import User

from jsonfield.fields import JSONField


class Log(models.Model):
    
    user = models.ForeignKey(User, null=True)
    timestamp = models.DateTimeField(default=datetime.now)
    action = models.CharField(max_length=50)
    extra = JSONField(default="{}")


def log(user, action, extra):
    if (user is not None and not user.is_authenticated()):
        user = None
    
    return Log.objects.create(user=user, action=action, extra=extra)
