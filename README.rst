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


Documentation
-------------

Documentation can be found at http://eventlog.rtfd.org/


Commercial Support
------------------

This app, and many others like it, have been built in support of many of Eldarion's
own sites, and sites of our clients. We would love to help you on your next project
so get in touch by dropping us a note at info@eldarion.com.