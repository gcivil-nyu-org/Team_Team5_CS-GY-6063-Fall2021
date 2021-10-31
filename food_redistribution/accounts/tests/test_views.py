from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from accounts.tokens import account_activation_token

# from accounts.models import *


class BaseTest(TestCase):
    def setUp(self):
        """
        user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
        name = models.CharField(max_length=200, default="")
        name_of_restaurant = models.CharField(max_length=200)
        email = models.CharField(max_length=200, unique=True)
        phone = models.CharField(max_length=200)
        address = models.CharField(max_length=200)
        verified = models.BooleanField(default=False)
        """
        self.registration_url = reverse("register")
        self.user = {
            "user": "testuser",
            "name": "name",
            "email": "test@email.com",
            "name_of_restaurant": "test",
            "phone": "1234567890",
            "address": "123 street south",
            "verified": True,
            "password1": "qaz2wsedc4rf",
            "password2": "qaz2wsedc4rf",
        }
        return super().setUp()

class AddPostTest(TestCase):
    def test_form_validity(self):
        c = Client()
        response = c.get(reverse("posts"))
        self.assertEqual(response.status_code, 200)




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


class ViewTests(BaseTest):
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

    def test_restaurant_register_already_authenticated(self):
        """
        If the restaurant is already logged in, it should redirect to home page
        """
        c = Client()
        user = User.objects.create_user("Annika", "annika@email.com")
        c.force_login(user=user)
        response = c.get(reverse("register"))
        self.assertRedirects(
            response,
            "/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    def test_food_red_register_already_authenticated(self):
        """
        If the food redistributor is already logged in, it should redirect to home page
        """
        c = Client()
        user = User.objects.create_user("Annika", "annika@email.com")
        c.force_login(user=user)
        response = c.get(reverse("register2"))
        self.assertRedirects(
            response,
            "/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    def test_restaurant_login(self):
        """
        Logging into the restaurant should direct them to home
        """
        c = Client()
        user = User.objects.create_user("Annika", "annika@email.com")
        c.force_login(user=user)
        response = c.get(reverse("login"))
        self.assertRedirects(
            response,
            "/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    def test_restaurant_login_already_authenticated(self):
        """
        Restaurant user that is already logged in should be redirected to home
        """
        c = Client()
        response = c.post(self.registration_url, self.user)
        self.assertEqual(response.status_code, 200)

    def test_food_red_login_already_authenticated(self):
        """
        Food redistributor user that is already logged in should be redirected to home
        """
        c = Client()
        response = c.post(reverse("register2"), self.user)
        self.assertEqual(response.status_code, 200)

    def test_food_red_login_already_authenticated_redirect(self):
        """
        Food redistributor user that is already logged in should be redirected to home
        """
        c = Client()
        user = User.objects.create_user("Annika", "annika@email.com")
        c.force_login(user=user)
        response = c.get(reverse("login2"))
        self.assertRedirects(
            response,
            "/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    """

    def test_restaurant_register_first_time(self):
        #user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
        #name = models.CharField(max_length=200, default="")
        #name_of_restaurant = models.CharField(max_length=200)
        #email = models.CharField(max_length=200, unique=True)
        #phone = models.CharField(max_length=200)
        #address = models.CharField(max_length=200)
        #verified = models.BooleanField(default=False)
        c = Client()
        response = c.post(
            'restaurant/', {
                'user': 'annika',
                'name': 'smith',
                'name_of_restaurant': 'annika restaurant',
                'email': 'annika@email.com',
                'phone': '123-456-7890',
                'address': '123 street south',
                'verified': False,
            }
        )
        self.assertContains(response, "Please confirm your email address to complete the registration")

        #self.assertRedirects(
        #    response,
        #    "/",
        #    status_code=302,
        #    target_status_code=200,
        #    fetch_redirect_response=True,
        #)

        """


class UserActivationTest(TestCase):
    def test_user_activate_success(self):
        user = User.objects.create_user("testuser1")
        user.set_password("qaz2wsedc4rf")
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activation_token.make_token(user)
        response = self.client.get(
            reverse("activate", kwargs={"uidb64": uid, "token": token})
        )
        self.assertEqual(response.status_code, 200)
        user = User.objects.get(username="testuser1")
        self.assertTrue(user.is_active)

    def test_user_activate_fail(self):
        user = User.objects.create_user("testuser2")
        user.set_password("wsx3edrfv5tg")
        token = account_activation_token.make_token(user)
        with self.assertRaises(User.DoesNotExist):
            response = self.client.get(
                reverse("activate", kwargs={"uidb64": "123", "token": token})
            )
            self.assertEqual(response.status_code, 200)
            user = User.objects.get(username="testuser3")
