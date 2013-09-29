.. _usage:

Usage
=====

Using ``eventlog`` is pretty simple. Throughout your site, you just call
a single function, ``log()`` to record whatever information you want to
log. If you are wanting to log things from third party apps, your best
bet is to use signals. Hopefully the app in question provides some useful
signals, but if not, perhaps some of the built in model signals will be
enough (e.g. ``pre_save``, ``post_delete``, etc.)

Example::

    from eventlog.models import log

    def some_view(request):
        # stuff is done in body of view
        # then at the end before returning the response:
        log(
            user=request.user,
            action="CREATED_FOO_WIDGET",
            extra={
                "pk": foo.pk,
                "title": foo.title
            }
        )
        return HttpResponse()


The ``action`` parameter can be any string you choose. By convention, we
always use all caps. Take note, however, whatever you choose, will be the
label that appears in the admin's list filter, so give it some thought on
naming conventions in your site so that the admin interface makes sense
when you have 50,000 log records you want to filter down and analyze.

The ``extra`` parameter can be anything that will serialize to JSON. Results
become easier to manager if you keep it at a single level. Also, keep in
mind that this is displayed in the admin's list view so if you put too much
it can take up a lot of space. A good rule of thumb here is put enough
identifying data to get a sense for what is going on and a key or keys
that enable you to dig deeper if you want or need to.
