from django.urls import path
from . import views


urlpatterns = [
    path('restaurant/', views.register_restaurant, name='register'),
    path('foodredis/', views.register_foodredistributor, name='register2'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
]
