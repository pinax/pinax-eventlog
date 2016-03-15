========
Pinax Eventlog
========

.. image:: http://slack.pinaxproject.com/badge.svg
   :target: http://slack.pinaxproject.com/

.. image:: https://img.shields.io/travis/pinax/pinax-eventlog.svg
    :target: https://travis-ci.org/pinax/pinax-eventlog

.. image:: https://img.shields.io/coveralls/pinax/pinax-eventlog.svg
    :target: https://coveralls.io/r/pinax/pinax-eventlog

.. image:: https://img.shields.io/pypi/dm/pinax-eventlog.svg
    :target:  https://pypi.python.org/pypi/pinax-eventlog/

.. image:: https://img.shields.io/pypi/v/pinax-eventlog.svg
    :target:  https://pypi.python.org/pypi/pinax-eventlog/

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target:  https://pypi.python.org/pypi/pinax-eventlog/
    
Pinax
------

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. 
This collection can be found at http://pinaxproject.com.

This app was developed as part of the Pinax ecosystem but is just a Django app and can be used independently of other Pinax apps.


pinax-eventlog
---------------

``pinax-eventlog`` is a simple app that provides an easy and clean
interface for logging diagnostic as well as business intelligence
data about activity that occurs in your site.

Out of the box using this does write to the database.

For small sites, it should be good enough to use inline but you might at some
point want to consider wrapping calls to the ``log()`` method and queue them in
a job manager like ``celery`` or ``pyres`` so that the calls become asynchronous.


History
-------

This project was originally named ``eventlog`` and was created by the team at
Eldarion. It was later donated to Pinax and at that time renamed to
``pinax-eventlog``.


Documentation
-------------

The ``pinax-eventlog`` documentation can be found at http://pinax-eventlog.rtfd.org/.
The Pinax documentation is available at http://pinaxproject.com/pinax/. If you would like to help us improve our documentation or write more documentation, please join our Pinax Project Slack team and let us know!


Contribute
----------------

See this blog post http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/ including a video, or our How to Contribute (http://pinaxproject.com/pinax/how_to_contribute/) section for an overview on how contributing to Pinax works. For concrete contribution ideas, please see our Ways to Contribute/What We Need Help With (http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any questions we recommend you join our Pinax Slack team (http://slack.pinaxproject.com) and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course also valid but we are usually able to help you faster if you ping us in Slack.

We also highly recommend reading our Open Source and Self-Care blog post (http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).  


Code of Conduct
----------------

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a code of conduct, which can be found here  http://pinaxproject.com/pinax/code_of_conduct/. 
We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.



Pinax Project Blog and Twitter
--------------------------------

For updates and news regarding the Pinax Project, please follow us on Twitter at @pinaxproject and check out our blog http://blog.pinaxproject.com.





