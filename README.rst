========
eventlog
========

.. image:: https://img.shields.io/travis/eldarion/eventlog.svg
    :target: https://travis-ci.org/eldarion/eventlog

.. image:: https://img.shields.io/coveralls/eldarion/eventlog.svg
    :target: https://coveralls.io/r/eldarion/eventlog

.. image:: https://img.shields.io/pypi/dm/eventlog.svg
    :target:  https://pypi.python.org/pypi/eventlog/

.. image:: https://img.shields.io/pypi/v/eventlog.svg
    :target:  https://pypi.python.org/pypi/eventlog/

.. image:: https://img.shields.io/badge/license-BSD-blue.svg
    :target:  https://pypi.python.org/pypi/eventlog/


``eventlog`` is a simple app that provides an easy and clean
interface for logging diagnostic as well as business intelligence
data about activity that occurs in your site.

Out of the box using this does write to the database.

For small sites, it should be good enough to use inline but you might at some point want to consider wrapping calls to the ``log()`` method and queue them in
a job manager like ``celery`` or ``pyres`` so that the calls become asynchronous.


Documentation
-------------

Documentation can be found at http://eventlog.rtfd.org/


Commercial Support
------------------

This app, and many others like it, have been built in support of many of Eldarion's
own sites, and sites of our clients. We would love to help you on your next project
so get in touch by dropping us a note at info@eldarion.com.
