from django.urls import path
from . import views


urlpatterns = [
    path('restaurant/', views.register_restaurant, name='register'),
    path('foodredis/', views.register_foodredistributor, name='register2'),
    path('restuarantlogin/', views.login_restuarant, name="login"),
    path('foodredislogin/', views.login_foodredistributor, name="login2"),
    path('restuarantlogout/', views.logout_restuarant, name="logout"),
    path('foodredislogout/', views.logout_foodredistributor, name="logout2"),

    path('', views.home, name="home"),
]