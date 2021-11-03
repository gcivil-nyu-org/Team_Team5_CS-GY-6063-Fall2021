from django.test import TestCase
from cal.forms import EventForm


class TestForms(TestCase):
    def test_EventForm_valid_data(self):
        form = EventForm(
            data={
                "start_time": "2021-10-29T19:30",
                "end_time": "2021-10-29T21:30",
                "title": "Testing a new event!",
                "description": "I wanna check if this thing really works",
            }
        )
        self.assertTrue(form.is_valid())
