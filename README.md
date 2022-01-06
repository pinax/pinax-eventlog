![](http://pinaxproject.com/pinax-design/patches/pinax-eventlog.svg)

# Pinax Eventlog

[![](https://img.shields.io/pypi/v/pinax-eventlog.svg)](https://pypi.python.org/pypi/pinax-eventlog/)

[![CircleCi](https://img.shields.io/circleci/project/github/pinax/pinax-eventlog.svg)](https://circleci.com/gh/pinax/pinax-eventlog/)
[![Codecov](https://img.shields.io/codecov/c/github/pinax/pinax-eventlog.svg)](https://codecov.io/gh/pinax/pinax-eventlog/)
[![](https://img.shields.io/github/contributors/pinax/pinax-eventlog.svg)](https://github.com/pinax/pinax-eventlog/graphs/contributors)
[![](https://img.shields.io/github/issues-pr/pinax/pinax-eventlog.svg)](https://github.com/pinax/pinax-eventlog/pulls)
[![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-eventlog.svg)](https://github.com/pinax/pinax-eventlog/pulls?q=is%3Apr+is%3Aclosed)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)


## Table of Contents

* [About Pinax](#about-pinax)
* [Important Links](#important-links)
* [Overview](#overview)
  * [Supported Django and Python Versions](#supported-django-and-python-versions)
* [Documentation](#documentation)
  * [Installation in Django >=3.1](#installation-in-django-31)
  * [Installation in Django <3.1](#installation-in-django-31-1)
  * [Usage](#usage)
  * [Signals](#signals)
* [Change Log](#change-log)
* [History](#history)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)
* [Connect with Pinax](#connect-with-pinax)
* [License](#license)


## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.


## Important Links

Where you can find what you need:
* Releases: published to [PyPI](https://pypi.org/search/?q=pinax) or tagged in app repos in the [Pinax GitHub organization](https://github.com/pinax/)
* Global documentation: [Pinax documentation website](https://pinaxproject.com/pinax/)
* App specific documentation: app repos in the [Pinax GitHub organization](https://github.com/pinax/)
* Support information: [SUPPORT.md](https://github.com/pinax/.github/blob/master/SUPPORT.md) file in the [Pinax default community health file repo](https://github.com/pinax/.github/)
* Contributing information: [CONTRIBUTING.md](https://github.com/pinax/.github/blob/master/CONTRIBUTING.md) file in the [Pinax default community health file repo](https://github.com/pinax/.github/)
* Current and historical release docs: [Pinax Wiki](https://github.com/pinax/pinax/wiki/)


## pinax-eventlog

### Overview

`pinax-eventlog` is a simple app that provides an easy and clean interface for logging diagnostic as well as business intelligence data about activity that occurs in your site.

By default this app writes directly to the database.

For small sites, it should be good enough to use inline but you might want to consider wrapping calls to the `log()` method and queue them in
a job manager like `celery` or `pyres` so that the calls become asynchronous.

#### Supported Django and Python versions

Django / Python | 3.6 | 3.7 | 3.8
--------------- | --- | --- | ---
2.2*  |  *  |  *  |  *
3.0*  |  *  |  *  |  *
3.1  |  *  |  *  |  *

_*see Installation in Django < 3.1 below*_

## Documentation

### Installation in Django >=3.1

To install pinax-eventlog:

```shell
    $ pip install pinax-eventlog
```

Add `pinax.eventlog` to your `INSTALLED_APPS` setting:

```python
    INSTALLED_APPS = [
        # other apps
        "pinax.eventlog",
    ]
```

Run the app's migrations:

```shell
    $ python manage.py migrate eventlog
```

### Installation in Django <3.1

Django 3.1 introduced a JSON model field on all supported backends:

https://docs.djangoproject.com/en/3.1/releases/3.1/#jsonfield-for-all-supported-database-backends

To use `pinax-eventlog` on sites running Django 2.2 and 3.0, you'll want to install the package with the
`django-lts` extra:

```shell
    $ pip install pinax-eventlog[django-lts]
```

Add `pinax.eventlog` and `django_jsonfield_backport` to your `INSTALLED_APPS` setting:

```python
    INSTALLED_APPS = [
        # other apps
        "django_jsonfield_backport,
        "pinax.eventlog",
    ]
```

Run the app's migrations:

```shell
    $ python manage.py migrate eventlog
```

### Usage

Using `pinax-eventlog` is pretty simple. Throughout your site, you just call a single function, `log()` to record whatever information you want to log. If you are wanting to log things from third party apps, your best bet is to use signals. Hopefully the app in question provides some useful signals, but if not, perhaps some of the built in model signals will be enough (e.g. `pre_save`, `post_delete`, etc.)

Example:

```python
from pinax.eventlog.models import log

def some_view(request):
    # stuff is done in body of view
    # then at the end before returning the response:
    log(
        user=request.user,
        action="CREATED_FOO_WIDGET",
        obj=foo,
        extra={
            "title": foo.title
        }
    )
    return HttpResponse()
```

The `action` parameter can be any string you choose. By convention, we
always use all caps. Take note, however, whatever you choose, will be the
label that appears in the admin's list filter, so give it some thought on
naming conventions in your site so that the admin interface makes sense
when you have 50,000 log records you want to filter down and analyze.

The `extra` parameter can be anything that will serialize to JSON. Results
become easier to manage if you keep it at a single level. Also, keep in
mind that this is displayed in the admin's list view so if you put too much
it can take up a lot of space. A good rule of thumb here is put enough
identifying data to get a sense for what is going on and a key or keys
that enable you to dig deeper if you want or need to.

#### Mixin

You can also easily make your class based views auto-logged by using the
`pinax.eventlog.mixins.EventLogMixin`. The only requirement is defining an
`action_kind` property on the view. But you can also override a number of
properties to customize what is logged.

### Signals

There is a signal that you are setup a receiver for to enable you to trigger
other actions when an event has been logged:

`event_logged` provides an `event` object as an argument that is the event that
was just logged.


## Change Log

### 5.1.1

* Remove deprecated `providing_args` argument ([Deprecated in Django 3.1](https://docs.djangoproject.com/en/4.0/releases/3.1/#id2))

### 5.1.0

* Restore Django 2.2 and 3.0 support via [`django-jsonfield-backport`](https://github.com/laymonage/django-jsonfield-backport)

### 5.0.0

* Switch to Django 3.1's JSONField
* Reset migrations _(see discussion in [#33](https://github.com/pinax/pinax-eventlog/issues/32#issuecomment-674414709))_

### 4.0.1

* Update `models.py` to support MySQL `JSONField`

### 4.0.0

* Drop Django 1.11, 2.0, and 2.1, and Python 2,7, 3.4, and 3.5 support
* Add Django 2.2 and 3.0, and Python 3.6, 3.7, and 3.8 support
* Update packaging configs
* Direct users to community resources

### 3.0.0

### 2.0.3

* Use SET_NULL so Log instances are not deleted when related object is deleted
* Update runtests.py
* Update CI configuration
* Update jsonfield requirement

### 2.0.2

* fix setup.py LONG_DESCRIPTION for PyPi

### 2.0.1

* Standardize and improve documentation

### 2.0.0

* Add Django 2.0 compatibility testing
* Drop Django 1.8, 1.9, 1.10 and Python 3.3 support
* Convert CI and coverage to CircleCi and CodeCov
* Add PyPi-compatible long description
* Move documentation to README.md

### 1.1.2

* Fix spelling error in documentation
* Added wheel release
* Dropped 3.2 support

### 1.1.1

* Added missing migration from the switch to jsonfield

### 1.1.0

* Started testing against Django master
* Switched to `jsonfield` from `django-jsonfield`
* Added ability to link a log to any object via a GFK
* Added ability to override timestamp
* Fixed template fragment path

### 1.0.0

* Eldarion donated to Pinax, renaming from `eventlog` to `pinax-eventlog`

### 0.11.0

* added the ability to link content objects you are logging about

### 0.10.0

* added property to provide template fragment name

### 0.9.0

* Add mixin for making it easy to audit CBV

### 0.8.0

* removed non-working templatetag
* update setup to work with Python 3.3+

### 0.7.0

* remove pusher integration
* support for custom user model

### 0.6.7

* added the `event_logged` signal
* corrected typo in usage documentation

### 0.6.6

* attempts at fixing admin performance

### 0.6.5

* attempts at fixing admin performance

### 0.6.4

* attempts at fixing admin performance with an index on action

### 0.6.3

* attempts at fixing admin performance with an index on timestamp

### 0.6.2

* update setup.py to use install_requires instead of setup_requires

### 0.6.1

* made the extra argument optional

### 0.6.0

* improve the admin

### 0.5.5

* use `django.utils.timezone.now` instead of `datetime.datetime.now` for timestamp

### 0.5.4

* when a user is deleted set FK to null instead of losing data

### 0.5.3

* bumped version on django-jsonfield

### 0.5.2

* added docs

### 0.5.1

* initial release


## History

This project was originally named `eventlog` and was created by the team at [Eldarion](http://eldarion.com). It was later donated to Pinax and at that time renamed to `pinax-eventlog`.


## Contribute

[Contributing](https://github.com/pinax/.github/blob/master/CONTRIBUTING.md) information can be found in the [Pinax community health file repo](https://github.com/pinax/.github).


## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a [Code of Conduct](https://github.com/pinax/.github/blob/master/CODE_OF_CONDUCT.md). We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


## Connect with Pinax

For updates and news regarding the Pinax Project, please follow us on Twitter [@pinaxproject](https://twitter.com/pinaxproject) and check out our [Pinax Project blog](http://blog.pinaxproject.com).


## License

Copyright (c) 2012-present James Tauber and contributors under the [MIT license](https://opensource.org/licenses/MIT).
