from django.test import TestCase
from food_avail.models import User, FoodAvail, TimeSlot


class test_FoodAvail(TestCase):
    def test_setUp(self):
        self.user = User.objects.create_user(
            username="john", email="jlennon@beatles.com", password="glass onion"
        )
        self.foodavail1 = FoodAvail.objects.create(
            food_available=10, description="We have food", author=self.user,
        )


class test_TimeSlot(TestCase):
    def test_setUp(self):
        self.user = User.objects.create_user(
            username="john", email="jlennon@beatles.com", password="glass onion"
        )
        self.timeslot1 = TimeSlot.objects.create(
            time_slot_owner=self.user, start_time="19:30", end_time="21:30",
        )
