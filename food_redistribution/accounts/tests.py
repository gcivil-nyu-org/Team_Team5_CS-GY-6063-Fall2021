from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from food_redistribution.settings import SECRET_KEY
import json

class AddAccountsViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("restaurant/")
        self.assertEqual(response.status_code, 200)
        self.t:


