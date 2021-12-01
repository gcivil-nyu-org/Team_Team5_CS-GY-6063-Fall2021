from django.urls import path
from food_avail import views

app_name = "food_avail"

urlpatterns = [
    path("post_food_avail/", views.post_available_food, name="post_food_avail"),
    path("food_avail_all/", views.check_food_availibility, name="view_food_avail"),
    path("food_avail_res/", views.view_available_food, name="view_food_avail_res"),
    path("update_time_slot/<int:pk>/", views.update_time_slot, name="update_time_slot"),
    path("delete_time_slot/<int:pk>/", views.delete_time_slot, name="delete_time_slot"),
    path("bookings/", views.bookings, name="bookings"),
    path("create_bookings/", views.create_booking, name="create_booking"),
    path("view_bookings/", views.view_bookings, name="view_bookings"),
    path("delete_booking/<int:pk>/", views.delete_booking, name="delete_booking"),
]
