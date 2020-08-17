from datetime import timedelta

import django
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.utils import timezone

from ..compat import JSONField
from ..mixins import EventLogMixin
from ..models import Log, log
from ..signals import event_logged
from ..stats import stats, used_active


class TestStats(TestCase):

    def setUp(self):
        user = get_user_model().objects.create(
            date_joined=(timezone.now() - timedelta(days=100))
        )
        log(action="SOME_EVENT", user=user, extra={})

    def test_used_active(self):
        used, active = used_active(10)
        self.assertEquals(used, 1)
        self.assertEquals(active, 1)

    def test_stats(self):
        data = stats()
        self.assertEquals(data, {
            "used_seven": 1,
            "used_thirty": 1,
            "active_seven": 1,
            "active_thirty": 1
        })


class TestModels(TestCase):

    def test_template_fragment_name(self):
        event = log(user=None, action="FOO")
        self.assertEquals(event.template_fragment_name, "pinax/eventlog/foo.html")

    def test_log_user_not_authed(self):
        user = AnonymousUser()
        event = log(user=user, action="FOO", extra={})
        self.assertIsNone(event.user)

    def test_log_extra_not_provided(self):
        event = log(user=None, action="FOO")
        self.assertEquals(event.extra, {})

    def test_log_content_object(self):
        user = get_user_model().objects.create(
            date_joined=(timezone.now() - timedelta(days=100))
        )
        event = log(user=None, action="FOO", obj=user)
        self.assertEquals(event.object_id, user.pk)
        self.assertEquals(event.content_type, ContentType.objects.get_for_model(user))

    def test_log_dateof(self):
        dateof = timezone.now() - timedelta(days=3)
        event = log(user=None, action="FOO", dateof=dateof)
        self.assertEquals(event.timestamp, dateof)

    def test_signal_sent(self):
        def _handler(sender, event, **kwargs):
            self.assertEquals(event.action, "FOO_SENT")
            event.sent = True

        event_logged.connect(_handler)
        event = log(user=None, action="FOO_SENT")
        self.assertTrue(event.sent)


class RequestMock:
    def __init__(self, user):
        self.user = user


class TestMixins(TestCase):

    def test_action(self):
        mixin = EventLogMixin()
        mixin.action_kind = "CREATE"
        mixin.model = get_user_model()
        self.assertEquals(mixin.action, "CREATE_USER")

    def test_extra_data(self):
        self.assertEquals(EventLogMixin().extra_data, {})

    def test_user(self):
        user = get_user_model().objects.create(
            date_joined=(timezone.now() - timedelta(days=100))
        )
        mixin = EventLogMixin()
        mixin.request = RequestMock(user)
        self.assertEquals(mixin.user, user)

    def test_log_action(self):
        user = get_user_model().objects.create(
            date_joined=(timezone.now() - timedelta(days=100))
        )
        mixin = EventLogMixin()
        mixin.action_kind = "CREATE"
        mixin.model = get_user_model()
        mixin.request = RequestMock(user)
        mixin.log_action()
        self.assertEquals(Log.objects.all()[0].action, "CREATE_USER")


class TestCompat(TestCase):  # noqa
    def test_jsonfield(self):
        if django.VERSION < (3, 1):
            from django_jsonfield_backport.models import \
                JSONField as BackportJSONField  # noqa
            assert JSONField == BackportJSONField
        if django.VERSION >= (3, 1):
            from django.db.models import \
                JSONField as SupportedJSONField  # noqa
            assert JSONField == SupportedJSONField
