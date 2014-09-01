from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework.test import APIRequestFactory

from eventlog.views import LogEventCreate
from eventlog.models import Log


class TestAPI(TestCase):
    def setUp(self):
        # Simple mocking data
        self.action = "action"
        self.extra_first = "first"
        self.extra_second = "second"
        self.user = User.objects.create(username="username",
                                        password="password",
                                        email="eldarion@eldarion.com")
        self.log = {
            "user": User.objects.get(username="username").id,
            "action": self.action,
            "extra": {
                "first": self.extra_first,
                "second": self.extra_second,
            }
        }

    def tearDown(self):
        # Destroy the created user for `setUp` method
        User.objects.get(username='username').delete()

    def test_log_create(self):
        """
        Test the API for creating a event log item
        """
        url = reverse("eventlog_api_add")
        factory = APIRequestFactory()
        view = LogEventCreate.as_view()

        # Using `json` because of `JSONRenderer` used by `LogEventCreate` view
        request = factory.post(url, self.log, format="json")
        response = view(request)

        self.assertEqual(response.status_code, 201)

        # Making sure `Log` item has been created
        log = Log.objects.all()[0]

        self.assertEqual(log.user, self.user)
        self.assertEqual(log.action, self.action)
        self.assertEqual(log.extra, self.log['extra'])
