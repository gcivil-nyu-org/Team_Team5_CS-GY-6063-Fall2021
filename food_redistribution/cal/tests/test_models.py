from django.test import TestCase
from cal.models import Event
from accounts.models import User


class TestEvent(TestCase):
    def test_setUp(self):
        user = User.objects.create_user(
            username="john", email="jlennon@beatles.com", password="glass onion"
        )
        self.event = Event.objects.create(
            title="new event!",
            description="Hey, I am testing a new event!",
            start_time="2021-10-29T19:30",
            end_time="2021-10-29T21:30",
            author=user,
        )
