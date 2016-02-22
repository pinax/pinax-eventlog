# pinax-eventlog

!!! note "Pinax Ecosystem"
    This app was developed as part of the Pinax ecosystem but is just a Django app
    and can be used independently of other Pinax apps.

    To learn more about Pinax, see <http://pinaxproject.com/>

`pinax-eventlog`, formerly named `eventlog` is a simple app that provides an
easy and clean interface for logging diagnostic as well as business
intelligence data about activity that occurs in your site.

Out of the box using this does write to the database. For small sites,
it should be good enough to use inline but you might at some point want to
consider wrapping calls to the `log()` method and queue them in a job manager
like `celery` or `pyres` so that the calls become asynchronous.


## Development

The source repository can be found at https://github.com/pinax/pinax-eventlog/


## Quickstart

Install the package:

    pip install pinax-eventlog

Add `pinax.eventlog` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        # other apps
        "pinax.eventlog",
    )

Run the app's migrations:

    python manage.py migrate eventlog
