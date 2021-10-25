from django.urls import path, include
from . import views
from .views import PostView, DetailedblogView, AddPostView, UpdatePostView, DeletePostView
from django.conf.urls import url
from django.contrib.auth import views as auth_views
# from cal import views as cal_views

urlpatterns = [
    path('restaurant/', views.register_restaurant, name='register'),
    path('profile/', views.profile, name='profile'),
    path('foodredis/', views.register_foodredistributor, name='register2'),
    path('restuarantlogin/', views.login_restuarant, name="login"),
    path('foodredislogin/', views.login_foodredistributor, name="login2"),
    path('restuarantlogout/', views.logout_restuarant, name="logout"),
    path('foodredislogout/', views.logout_foodredistributor, name="logout2"),

    path(
        'reset_password/',
        auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
        name="reset_password"),

    path(
        'reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
        name="password_reset_done"),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
        name="password_reset_confirm"),

    path(
        'reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"),
        name="password_reset_complete"),

    path('', views.home, name="home"),
    path('calendar/', include(('cal.urls', 'cal'), namespace='calendar')),

    path('blogposts/',PostView.as_view(), name = "posts"),
    path('blogposts/<int:pk>', DetailedblogView.as_view(), name = "blog-details"),
    path('addpost/', AddPostView.as_view(), name = "add-post"),
    path('blogposts/edit/<int:pk>', UpdatePostView.as_view(), name = 'update_post'),
    path('blogposts/<int:pk>/remove', DeletePostView.as_view(), name = 'delete_post'),

    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,6}-[0-9A-Za-z]{1,32})/$',
        views.activate, name='activate'),
]
