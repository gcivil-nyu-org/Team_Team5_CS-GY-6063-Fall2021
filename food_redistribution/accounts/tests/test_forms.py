from django.test import TestCase
from accounts.forms import RestuarantUserForm, FoodRedistributorUserForm, PostForm
from accounts.models import User, Post


class TestForms(TestCase):
    def test_restaurantUserForm_valid_data(self):
        form = RestuarantUserForm(
            data={
                "name_of_restaurant": "Woodbricks oven",
                "email": "woodbricks@email.com",
                "username": "woodbricks",
                "phone": "24364696",
                "address": "Erie street,jersey",
                "password1": "test@1234",
                "password2": "test@1234",
            }
        )

        self.assertTrue(form.is_valid())

    def test_restaurantUserForm_no_data(self):
        form = RestuarantUserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 7)

    def test_foodRedistributorUserForm_valid_data(self):
        form = FoodRedistributorUserForm(
            data={
                "name_of_food_redis": "Food bank of NYC",
                "email": "foodbank@email.com",
                "username": "foodbank",
                "phone": "12345678",
                "address": "canal street nyc",
                "password1": "test@1234",
                "password2": "test@1234",
            }
        )

        self.assertTrue(form.is_valid())

    def test_foodRedistributorUserForm_no_data(self):
        form = FoodRedistributorUserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 7)


class TestBlogPostForms(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="john", email="jlennon@beatles.com", password="glass onion"
        )
    def test_form_valid(self):
        form = PostForm(
            data={
            "title": "Test title",
            "author": self.user,
            "body": "Test body",
        }
        )
        self.assertTrue(form.is_valid())    