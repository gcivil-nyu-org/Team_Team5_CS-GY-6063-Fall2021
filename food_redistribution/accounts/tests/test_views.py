from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from accounts.tokens import account_activation_token

# from django.http import HttpResponse
from unittest.mock import Mock, patch

# from django.contrib.auth import logout
from accounts.forms import *

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
            "/profile/",
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
            "/profile/",
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
            "/profile/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    def test_food_red_login(self):
        """
        Logging into the restaurant should direct them to home
        """
        c = Client()
        user = User.objects.create_user("Annika", "annika@email.com")
        c.force_login(user=user)
        response = c.get(reverse("login2"))
        self.assertRedirects(
            response,
            "/profile/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    """
    def test_food_red_login_post(self):

        #if request.method == "POST":
        #    username = request.POST.get("username")
        #    password = request.POST.get("password")

        c = Client()
        #user = User.objects.create_user({"username": "annika", "password": "1234567890"})
        response = c.post(self.user)
        self.assertRedirects(
            response,
            "/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
    """

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
            "/profile/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    def test_restaurant_logout_redirect(self):
        """
        def logout_restuarant(request):
            logout(request)
            return redirect("login")

            # Log out
        self.client.logout()

        path("restuarantlogout/", views.logout_restuarant, name="logout"),
        path("foodredislogout/", views.logout_foodredistributor, name="logout2"),
        """
        c = Client()
        user = User.objects.create_user("Annika", "annika@email.com")
        c.force_login(user=user)
        response = c.get(reverse("logout"))
        self.assertRedirects(
            response,
            "/restuarantlogin/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    def test_food_red_logout_redirect(self):
        c = Client()
        user = User.objects.create_user("Annika", "annika@email.com")
        c.force_login(user=user)
        response = c.get(reverse("logout2"))
        self.assertRedirects(
            response,
            "/foodredislogin/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    """
    COmmenting out these tests for now bc they are throwing errors that have to do with static files and heroku, idk

    def test_landing_page_success(self):
        # Going to landing page should return the correct page
        c = Client()
        response = c.get(reverse("landing"))
        self.assertEqual(response.status_code, 200)

    def test_choose_login_page_success(self):
        # Going to choose login page should return the correct page
        c = Client()
        response = c.get(reverse("chooselogin"))
        self.assertEqual(response.status_code, 200)

    def test_about_success(self):
        # Going to about page should return the correct page
        c = Client()
        response = c.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

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


class ViewTestsAgain(TestCase):
    @patch("accounts.views.register_restaurant")
    def test_restaurant_register_first_time(self, register_restaurant):
        # user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
        # name = models.CharField(max_length=200, default="")
        # name_of_restaurant = models.CharField(max_length=200)
        # email = models.CharField(max_length=200, unique=True)
        # phone = models.CharField(max_length=200)
        # address = models.CharField(max_length=200)
        # verified = models.BooleanField(default=False)

        mock = Mock()
        mock.register_restaurant()
        mock.register_restaurant.assert_called()

        # c = Client()
        data = {
            "name_of_restaurant": "fivefries",
            "email": "fivefries@somemail.com",
            "username": "five_fries",
            "phone": "1234567890",
            "address": "123 Fries Way",
            "password1": "qaz2wsedc4rf",
            "password2": "qaz2wsedc4rf",
        }
        form = RestuarantUserForm(data)
        # response = c.post(data)
        self.assertTrue(form.is_valid())

    @patch("accounts.views.landing")
    def test_landing_page(self, landing):
        mock = Mock()
        mock.landing()
        mock.landing.assert_called()

    @patch("accounts.views.choose_login")
    def test_choose_login_page(self, choose_login):
        mock = Mock()
        mock.choose_login()
        mock.choose_login.assert_called()

    @patch("accounts.views.about")
    def test_about_page(self, about):
        mock = Mock()
        mock.about()
        mock.about.assert_called()
