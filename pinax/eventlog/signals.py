import django.dispatch

event_logged = django.dispatch.Signal(providing_args=["event"])
