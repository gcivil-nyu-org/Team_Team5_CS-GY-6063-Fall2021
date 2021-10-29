from django.test import TestCase, Client
from django.urls import reverse

# from django.contrib.auth.models import User
# from accounts.models import *


class PostViewTest(TestCase):
    def test_no_posts(self):
        """
        If no posts exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("posts"))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "No polls are available.")


"""
class DetailedblogViewTest(TestCase):
    def test_detailed_post(self):

        # If you click on a post, it will show up.

        c = Client()
        user = User.objects.create_user("Annika", "annika@email.com")
        c.force_login(user=user)

        onepost = Post.objects.create(
            title = f'test title',
            author = user,
            body = f'test body',
            id = 1
        )
        #response = c.post(
        #    reverse("add-post"),
        #    data=onepost,
        #)
        response2 = self.client.get(reverse('blog-details/', args=(1,)))
        # self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.status_code, 302)
        self.assertEqual(response2.status_code, 200)
        # self.assertContains(response2, desc)
        # self.assertContains(response, "No polls are available.")
"""


class ViewTests(TestCase):
    def test_restaurant_register(self):
        """
        A get request to the restaurant registration page should yield a valid response
        """
        c = Client()
        response = c.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_food_red_register(self):
        """
        A get request to the food redistributor registration page should yield a valid response
        """
        c = Client()
        response = c.get(reverse("register2"))
        self.assertEqual(response.status_code, 200)
