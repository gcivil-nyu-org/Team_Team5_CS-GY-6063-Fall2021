from django.shortcuts import render

# from yelp_search.models import Restaurant
# from django.http import Http404
from .forms import LocationForm

import requests

# from django.contrib.auth.decorators import login_required

from urllib.parse import quote

import os
from accounts.models import Restaurant
from food_avail.models import FoodAvail

# from django.urls import reverse

api_key = str(os.getenv("YELP_API"))

API_HOST = "https://api.yelp.com"
SEARCH_PATH = "/v3/businesses/search"
BUSINESS_PATH = "/v3/businesses/"


# The index page
def base(request):
    context = {}
    form = LocationForm(request.POST or None)
    context["form"] = form
    return render(request, "yelp_search/base.html", context)


def search_restaurants(request):
    context = {}
    form = LocationForm(request.POST or None)
    location = request.POST["searched"]

    k = search(api_key, '"restaurant","food","public"', location, 20)
    data = []

    if not k.get("error"):
        data = k["businesses"]
        # Sort by distance
        data.sort(key=getDistance)

    context["form"] = form
    context["location"] = location
    context["data"] = data

    in_database = []
    meals_available = None
    for i in range(len(data)):
        if (
            len(Restaurant.objects.filter(phone=data[i]["phone"][2:])) > 0
        ):  # pragma: no cover
            res = Restaurant.objects.filter(phone=data[i]["phone"][2:])[
                0
            ]  # pragma: no cover
            in_database.append(res.phone)
            if len(FoodAvail.objects.filter(author=res.user)) > 0:
                meals_available = FoodAvail.objects.filter(author=res.user)[
                    0
                ].food_available
                context["data"][i]["meals_available"] = meals_available

    context["in_database"] = in_database
    context["meals"] = meals_available
    for i in range(len(context["data"])):
        context["data"][i]["phone"] = context["data"][i]["phone"][2:]
    return render(request, "yelp_search/search.html", context)


# Helper function: make an API request
def request(host, path, api_key, url_params=None):
    url_params = url_params or {}
    url = "{0}{1}".format(host, quote(path.encode("utf8")))
    headers = {
        "Authorization": "Bearer %s" % api_key,
    }
    response = requests.request("GET", url, headers=headers, params=url_params)
    return response.json()


# Helper function: fetch searched data with given parameters - search keywords
# as term, address as loaction, and number of data entries to fetch as num
def search(api_key, term, location, num):
    url_params = {
        "term": term.replace(" ", "+"),
        "location": location.replace(" ", "+"),
        "limit": num,
        "radius": 500,
    }
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


# Helper function: get distance from the searched location
def getDistance(restaurant_dic):
    return restaurant_dic["distance"]
