
from django.test import TestCase, Client
from django.urls import reverse


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
