from django.contrib.auth.models import User
from django.test import TestCase
from accounts.models import Post, Restaurant, FoodRedistributor


class test_FoodRedis(TestCase):
    def test_setUp(self):
        self.redis1 = FoodRedistributor.objects.create(
            name="Test username",
            name_of_food_redis="Test Redis",
            email="testemail@gmaili.com",
            phone=5849721452,
            address="Test address",
            verified=True,
        )


class test_Restaurant(TestCase):
    def test_setUp(self):
        self.rest1 = Restaurant.objects.create(
            name="Test username",
            name_of_restaurant="Test Rest",
            email="testemail@gmaili.com",
            phone=5849721452,
            address="Test address",
            verified=True,
        )


class test_Post(TestCase):
    def test_setUp(self):
        user = User.objects.create_user(
            username="john", email="jlennon@beatles.com", password="glass onion"
        )
        self.post1 = Post.objects.create(
            title="Test title", author=user, body="Test body"
        )

    def test_get_absolute_url(self):
        user = User.objects.create_user(
            username="john", email="jlennon@beatles.com", password="glass onion"
        )
        self.post1 = Post.objects.create(
            title="Test title", author=user, body="Test body"
        )
        self.assertEqual(
            self.post1.get_absolute_url(), "/blogposts/" + str(self.post1.id)
        )
