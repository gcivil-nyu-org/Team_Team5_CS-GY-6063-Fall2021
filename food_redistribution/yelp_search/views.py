from django.shortcuts import render
from yelp_search.models import Restaurant
from django.http import Http404
from .forms import LocationForm

import requests

# from django.contrib.auth.decorators import login_required

from urllib.parse import quote

import os

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

    # Load rating data from our database
    # for restroom in data:
    #    restroom["distance"] = int(restroom["distance"])
    # print(restroom["distance"])
    #    r_id = restroom["id"]
    #    querySet = Restroom.objects.filter(yelp_id=r_id)
    #    if not querySet:
    #        restroom["our_rating"] = "no rating"
    #        restroom["db_id"] = ""
    #    else:
    #        restroom["our_rating"] = querySet.values()[0]["rating"]
    #        restroom["db_id"] = querySet.values()[0]["id"]
    # print(restroom["db_id"])
    #    addr = str(restroom["location"]["display_address"])
    #    restroom["addr"] = addr.translate(str.maketrans("", "", "[]'"))

    context["form"] = form
    context["location"] = location
    context["data"] = data

    print("THE LOCATION WAS: ", context["location"])

    return render(request, "yelp_search/search.html", context)


def restaurant_detail(request, r_id):
    # show a single restaurant
    querySet = Restaurant.objects.filter(id=r_id)
    res = {}
    if querySet:
        yelp_id = querySet.values()[0]["yelp_id"]
        yelp_data = get_business(api_key, yelp_id)
        yelp_data["db_id"] = r_id
        yelp_data["rating"] = querySet.values()[0]["rating"]
        yelp_data["Accessible"] = querySet.values()[0]["Accessible"]
        yelp_data["FamilyFriendly"] = querySet.values()[0]["FamilyFriendly"]
        yelp_data["TransactionRequired"] = querySet.values()[0]["TransactionRequired"]

        res["yelp_data"] = yelp_data
        addr = str(yelp_data["location"]["display_address"])
        res["addr"] = addr.translate(str.maketrans("", "", "[]'"))
        res["desc"] = querySet.values()[0]["Description"]
    else:
        raise Http404("Restaurant does not exist")

    context = {"res": res}
    return render(request, "yelp_search/detail.html", context)


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


# Helper function: fetch one single business using the business id
def get_business(api_key, business_id):
    business_path = BUSINESS_PATH + business_id
    return request(API_HOST, business_path, api_key)


# Helper function: get distance from the searched location
def getDistance(restaurant_dic):
    return restaurant_dic["distance"]
