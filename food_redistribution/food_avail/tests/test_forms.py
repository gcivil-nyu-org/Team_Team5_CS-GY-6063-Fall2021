from django.test import TestCase
from food_avail.forms import FoodAvailForm, TimeSlotForm
from food_avail.models import User


class TestForms(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="john", email="jlennon@beatles.com", password="glass onion"
        )

    def test_FoodAvailForm_valid_data(self):
        form = FoodAvailForm(
            data={
                "food_available": "2021-10-29T19:30",
                "description": "2021-10-29T21:30",
                "author": self.user,
            }
        )
        self.assertTrue(form.is_valid())

    def test_TimeSlotForm_valid_data(self):
        form = TimeSlotForm(
            data={
                "time_slot_owner": self.user,
                "start_time": "19:30",
                "end_time": "21:30",
            }
        )
        self.assertTrue(form.is_valid())
