========
eventlog
========

``eventlog`` is a simple app that provides an easy and clean
interface for logging diagnostic as well as business intelligence
data about activity that occurs in your site.

Out of the box using this does write to the database. For small sites,
it should be good enough to use inline but you might at some point want to
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
 signals
 usage
