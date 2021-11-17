from django.urls import path
from food_avail import views

app_name = "food_avail"

urlpatterns = [
    # path("post_food_avail/", post_available_food, name="food_avail"),
    path("post_food_avail/", views.FoodAvailCreateView.as_view(), name="post_food_avail"),
    path("update_food_avail/", views.food_avail_update_view, name="update_food_avail"),
    path("food_avail_all/", views.check_food_availibility, name="view_food_avail"),
    path("food_avail_res/", views.view_available_food, name="view_food_avail_res"),
    path("timeslots/",  views.create_timeslots, name="create_timeslots"),

]
