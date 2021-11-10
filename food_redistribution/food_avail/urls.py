from django.urls import path
from food_avail.views import *

app_name = "food_avail"

urlpatterns = [
    path("post_food_avail/", post_available_food, name="food_avail"),
    path("food_avail/", check_food_availibility, name="view_food_avail"),
]
