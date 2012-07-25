.. _installation:

Installation
============

* To install ::
    
    pip install django-jsonfield
    pip install eventlog

* Add ``'eventlog'`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        # other apps
        "eventlog",
    )


Optionally
----------

* Configure Pusher::

    PUSHER_CONFIG = {
        "app_id": "<app_id>",
        "key": "<key>",
        "secret": "<secret>"
    }
