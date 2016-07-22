# ChangeLog

## 1.1.2

- Fix spelling error in documentation
- Added wheel release
- Dropped 3.2 support


## 1.1.1

 - Added missing migration from the switch to jsonfield


## 1.1.0

- Started testing against Django master
- Switched to `jsonfield` from `django-jsonfield`
- Added ability to link a log to any object via a GFK
- Added ability to override timestamp
- Fixed template fragment path


## 1.0.0

- Eldarion donated to Pinax, renaming from `eventlog` to `pinax-eventlog`


## 0.11.0

- added the ability to link content objects you are logging about


## 0.10.0

- added property to provide template fragment name


## 0.9.0

- Add mixin for making it easy to audit CBV


## 0.8.0

- removed non-working templatetag
- update setup to work with Python 3.3+


## 0.7.0

- remove pusher integration
- support for custom user model


## 0.6.7

- added the `event_logged` signal
- corrected typo in usage documentation


## 0.6.6

- attempts at fixing admin performance

## 0.6.5

- attempts at fixing admin performance


## 0.6.4

- attempts at fixing admin performance with an index on action


## 0.6.3

- attempts at fixing admin performance with an index on timestamp


## 0.6.2

- update setup.py to use install_requires instead of setup_requires


## 0.6.1

- made the extra argument optional


## 0.6.0

- improve the admin


## 0.5.5

- use `django.utils.timezone.now` instead of `datetime.datetime.now` for timestamp


## 0.5.4

- when a user is deleted set FK to null instead of losing data

## 0.5.3

- bumped version on django-jsonfield


## 0.5.2

- added docs


## 0.5.1

- initial release
