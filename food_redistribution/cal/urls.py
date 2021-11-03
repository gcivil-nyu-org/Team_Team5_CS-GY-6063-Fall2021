from django.conf.urls import url
from . import views

app_name = "cal"
urlpatterns = [
    url("index/", views.index, name="index"),
    url("calendar/", views.CalendarView.as_view(), name="calendar"),
    url("event/new/", views.event_create, name="event_new"),
    url(r"^event/edit/(?P<pk>\d+)/$", views.event_update, name="event_edit"),
    url(r"^event/delete/(?P<pk>\d+)/$", views.event_delete, name="event_delete"),
]
