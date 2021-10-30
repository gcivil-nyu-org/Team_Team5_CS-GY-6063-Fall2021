from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import Mock, patch


class TestViews(TestCase):
    def test_index(self):
        client = Client()
        response = client.get(reverse("cal:index"))
        self.assertEquals(response.status_code, 200)

    def test_get_date(self):
        client = Client()
        response = client.get(reverse("cal:calendar"))
        self.assertEquals(response.status_code, 200)

    def test_prev_month(self):
        client = Client()
        response = client.get(reverse("cal:calendar"))
        self.assertEquals(response.status_code, 200)

    def test_next_month(self):
        client = Client()
        response = client.get(reverse("cal:calendar"))
        self.assertEquals(response.status_code, 200)

    def test_event(self):
        client = Client()
        response = client.get(reverse("cal:event_new"))
        self.assertEquals(response.status_code, 200)

    @patch("cal.views.get_date")
    def test_get_date_function(self, get_date):
        mock = Mock()
        mock.get_date()
        mock.get_date.assert_called()

    @patch("cal.views.prev_month")
    def test_prev_month_function(self, prev_month):
        mock = Mock()
        mock.prev_month()
        mock.prev_month.assert_called()

    @patch("cal.views.next_month")
    def test_next_month_function(self, next_month):
        mock = Mock()
        mock.next_month()
        mock.next_month.assert_called()

    @patch("cal.views.event")
    def test_event_function(self, event):
        mock = Mock()
        mock.event()
        mock.event.assert_called()
