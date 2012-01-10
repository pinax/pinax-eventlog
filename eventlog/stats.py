from datetime import datetime, timedelta

from django.contrib.auth.models import User


def stats():
    return {
        "used_site_last_thirty_days": User.objects.filter(log__timestamp__gt=datetime.now() - timedelta(days=30)).distinct().count(),
        "used_site_last_seven_days": User.objects.filter(log__timestamp__gt=datetime.now() - timedelta(days=7)).distinct().count()
    }
