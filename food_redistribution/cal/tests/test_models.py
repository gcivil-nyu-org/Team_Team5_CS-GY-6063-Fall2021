from django.test import TestCase
from cal.models import Event


class TestEvent(TestCase):
    def setUp(self):
        self.event = Event.objects.create( # pragma: no cover
            title="new event!",
            description="Hey, I am testing a new event!",
            start_time="2021-10-29T19:30",
            end_time="2021-10-29T21:30",
        )
