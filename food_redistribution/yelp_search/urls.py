from django.conf.urls import url
from . import views

app_name = "yelp_search"
urlpatterns = [
    url(r"^base/$", views.base, name="base"),
    url(r"^search_restaurants/$", views.search_restaurants, name="search_restaurants"),
    # url(
    #    r"^restaurant_detail/<int:r_id>/$",
    #    views.restaurant_detail,
    #    name="restaurant_detail",
    # ),
]
