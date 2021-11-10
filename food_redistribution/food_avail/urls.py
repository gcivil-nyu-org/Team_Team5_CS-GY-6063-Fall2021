from django.urls import path, include
from food_avail.views import *
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("food_avail/", post_available_food, name="food_avail")

]