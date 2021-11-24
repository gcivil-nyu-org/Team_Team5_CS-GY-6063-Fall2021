from django.test import TestCase
from unittest.mock import Mock, patch
from food_avail.models import User, FoodAvail, TimeSlot


class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="john", email="jlennon@beatles.com", password="glass onion"
        )
        self.foodavail1 = FoodAvail.objects.create(
            food_available=10,
            description="We have food",
            author=self.user,
        )
        self.timeslot1 = TimeSlot.objects.create(
            time_slot_owner=self.user,
            start_time="19:30",
            end_time="21:30",
        )

    # def test_index(self):
    #     client = Client()
    #     response = client.get(reverse("cal:index"))
    #     self.assertEquals(response.status_code, 200)

    # def test_get_date(self):
    #     client = Client()
    #     response = client.get(reverse("cal:calendar"))
    #     self.assertEquals(response.status_code, 200)

    # def test_prev_month(self):
    #     client = Client()
    #     response = client.get(reverse("cal:calendar"))
    #     self.assertEquals(response.status_code, 200)

    # def test_next_month(self):
    #     client = Client()
    #     response = client.get(reverse("cal:calendar"))
    #     self.assertEquals(response.status_code, 200)

    # def test_post_available_food(self):
    #     client = Client()
    #     client.force_login(user=self.user)
    #     response = client.get(reverse("food_avail:post_food_avail"))
    #     self.assertEquals(response.status_code, 200)

    # def test_view_available_food(self):
    #     client = Client()
    #     client.force_login(user=self.user)
    #     response = client.get(reverse("food_avail:view_food_avail_res"))
    #     self.assertEquals(response.status_code, 200)

    # def test_event_update(self):
    #     client = Client()
    #     response = client.get(reverse("cal:event_edit", args=(self.event.pk,)))
    #     self.assertEquals(response.status_code, 200)

    # def test_event_delete(self):
    #     client = Client()
    #     response = client.get(reverse("cal:event_delete", args=(self.event.pk,)))
    #     self.assertEquals(response.status_code, 200)

    @patch("food_avail.views.check_existing_post")
    def test_check_existing_post(self, check_existing_post):
        mock = Mock()
        mock.check_existing_post()
        mock.check_existing_post.assert_called()
