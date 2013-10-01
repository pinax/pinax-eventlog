.. _changelog:

ChangeLog
=========

0.6.7
-----

- added the `event_logged` signal
- corrected typo in usage documentation

0.6.6
-----

- attempts at fixing admin performance

0.6.5
-----

- attempts at fixing admin performance


0.6.4
------

- attempts at fixing admin performance with an index on action


0.6.3
-----

- attempts at fixing admin performance with an index on timestamp


0.6.2
-----

- update setup.py to use install_requires instead of setup_requires


0.6.1
-----

- made the extra argument optional


0.6.0
-----

- improve the admin


0.5.5
-----

- use `django.utils.timezone.now` instead of `datetime.datetime.now` for timestamp


0.5.4
-----

- when a user is deleted set FK to null instead of losing data

0.5.3
-----

- bumped version on django-jsonfield


0.5.2
-----

- added docs


0.5.1
-----

- initial release
