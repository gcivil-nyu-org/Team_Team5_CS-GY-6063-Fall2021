from django.urls import path
from food_avail import views

app_name = "food_avail"

urlpatterns = [
    path("post_food_avail/", views.post_available_food, name="post_food_avail"),
    # path("post_food_avail/", views.FoodAvailCreateView.as_view(), name="post_food_avail"),
    # path("update_food_avail/", views.post_available_food, name="update_food_avail"),
    path("food_avail_all/", views.check_food_availibility, name="view_food_avail"),
    path("food_avail_res/", views.view_available_food, name="view_food_avail_res"),
    path("update_time_slot/<int:pk>/", views.update_time_slot, name="update_time_slot"),
    path("delete_time_slot/<int:pk>/", views.delete_time_slot, name="delete_time_slot"),
    path("create_bookings/", views.create_bookings, name="create_bookings"),
    # path("food_avail_res/",  views.post_available_timeslots, name="create_timeslots"),
]
