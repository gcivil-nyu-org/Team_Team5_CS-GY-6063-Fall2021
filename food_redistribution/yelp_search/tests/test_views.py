from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import Mock, patch


import os

api_key = str(os.getenv("YELP_API"))

API_HOST = "https://api.yelp.com"
SEARCH_PATH = "/v3/businesses/search"
BUSINESS_PATH = "/v3/businesses/"


class ViewTests(TestCase):
    def test_base(self):
        """
        A get request to the base page should yield a valid response
        """
        c = Client()
        response = c.get(reverse("yelp_search:base"))
        self.assertEqual(response.status_code, 200)

    def test_restaurant_invalid_search(self):
        """
        A search with an invalid search string should yield no results
        but should return a valid webpage
        """
        c = Client()
        response = c.post(
            reverse("yelp_search:search_restaurants"), data={"searched": "szzzzz"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Location Not Found")

    def test_restaurant_valid_search(self):
        """
        A search with an valid search string should yield results
        and a valid webpage
        """
        c = Client()
        response = c.post(
            reverse("yelp_search:search_restaurants"), data={"searched": "tandon"}
        )
        self.assertEqual(response.status_code, 200)

    @patch("yelp_search.views.search")
    def test_search_function(self, search):
        mock = Mock()
        mock.search()
        mock.search.assert_called()

    @patch("yelp_search.views.request")
    def test_request_function(self, request):
        mock = Mock()
        mock.request()
        mock.request.assert_called()

    # @patch("yelp_search.views.get_business")
    # def test_get_biz_function(self, get_business):
    #     mock = Mock()
    #     mock.get_business()
    #     mock.get_business.assert_called()

    @patch("yelp_search.views.getDistance")
    def test_get_distance(self, getDistance):
        """
        def getDistance(restaurant_dic):
            return restaurant_dic["distance"]
        """
        mock = Mock()
        mock.getDistance()
        mock.getDistance.assert_called()
