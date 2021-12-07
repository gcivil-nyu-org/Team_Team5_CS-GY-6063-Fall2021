from django.test import TestCase
from cal.forms import EventForm
from accounts.models import User


class TestForms(TestCase):
    def test_EventForm_valid_data(self):
        user = User.objects.create_user(
            username="john", email="jlennon@beatles.com", password="glass onion"
        )
        form = EventForm(
            data={
                "start_time": "2025-10-29T19:30",
                "end_time": "2025-10-29T21:30",
                "title": "Testing a new event!",
                "description": "I wanna check if this thing really works",
                "author": user,
                "category": "event",
            }
        )
        self.assertTrue(form.is_valid())
