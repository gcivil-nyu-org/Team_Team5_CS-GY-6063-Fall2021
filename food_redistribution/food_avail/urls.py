from django.urls import path
from food_avail.views import *

app_name = "food_avail"

urlpatterns = [
    path("post_food_avail/", post_available_food, name="food_avail"),
    path("food_avail_all/", check_food_availibility, name="view_food_avail"),
    path("food_avail_res/", view_available_food, name="view_food_avail_res"),
    path("timeslots/",  create_timeslots, name="create_timeslots"),

]
