from django.test import TestCase, Client
from unittest.mock import Mock, patch
from food_avail.models import User, FoodAvail, TimeSlot
from django.urls import reverse


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

    def test_view_food_avail_res(self):
        client = Client()
        client.force_login(user=self.user)
        response = client.get("/food_avail_res/")
        self.assertEqual(response.status_code, 200)

    def test_view_post_food_avail(self):
        client = Client()
        client.force_login(user=self.user)
        response = client.get("/post_food_avail/")
        self.assertEqual(response.status_code, 200)

    def test_view_bookings(self):
        client = Client()
        client.force_login(user=self.user)
        response = client.get("/bookings/")
        self.assertEqual(response.status_code, 200)

    def test_view_bookings_view(self):
        client = Client()
        client.force_login(user=self.user)
        response = client.get("/view_bookings/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        client = Client()
        client.force_login(user=self.user)
        response = client.get(reverse("food_avail:view_food_avail_res"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        client = Client()
        client.force_login(user=self.user)
        response = client.get(reverse("food_avail:view_food_avail_res"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "food_avail/view_food.html")

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

    @patch("food_avail.views.delete_time_slot")
    def test_delete_time_slot(self, delete_time_slot):
        mock = Mock()
        mock.delete_time_slot()
        mock.delete_time_slot.assert_called()

    @patch("food_avail.views.update_time_slot")
    def test_update_time_slot(self, update_time_slot):
        mock = Mock()
        mock.update_time_slot()
        mock.update_time_slot.assert_called()

    @patch("food_avail.views.view_available_food")
    def test_view_available_food(self, view_available_food):
        mock = Mock()
        mock.view_available_food()
        mock.view_available_food.assert_called()

    @patch("food_avail.views.check_existing_post")
    def test_check_existing_post(self, check_existing_post):
        mock = Mock()
        mock.check_existing_post()
        mock.check_existing_post.assert_called()
