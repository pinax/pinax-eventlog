========
eventlog
========

``eventlog`` is a simple app that provides an easy and clean
interface for logging diagnostic as well as business intelligence
data about activity that occurs in your site.

There is optional Pusher (http://pusher.com) support baked in so
that if you add a ``PUSHER_CONFIG`` to settings, your events will
also be sent to Pusher as well as your database. Using this feature
you can write a simple Pusher client to aggregate activity across
multiple sites in a dashboard showing live activity.

Out of the box using this does write to the database (and if Pusher
is enabled, write to an http connection). For small sites, it should
be good enough to use inline but you might at some point want to
consider wrapping calls to the ``log()`` method and queue them in
a job manager like ``celery`` or ``pyres`` so that the calls become
asyncronous.


Development
-----------

The source repository can be found at https://github.com/eldarion/eventlog/


Contents
========

.. toctree::
 :maxdepth: 1

 changelog
 installation
 templatetags
 usage
 
