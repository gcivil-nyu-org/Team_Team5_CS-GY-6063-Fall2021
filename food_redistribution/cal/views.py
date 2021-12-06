from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib import messages

import calendar

from .models import *
from .utils import Calendar
from .forms import EventForm


def index(request):
    return HttpResponse("hello")


class CalendarView(generic.ListView):
    model = Event
    template_name = "cal/calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get("month", None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context["calendar"] = mark_safe(html_cal)
        context["prev_month"] = prev_month(d)
        context["next_month"] = next_month(d)
        return context  # pragma: no cover


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split("-"))  # pragma: no cover
        return date(year, month, day=1)  # pragma: no cover
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = "month=" + str(prev_month.year) + "-" + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = "month=" + str(next_month.year) + "-" + str(next_month.month)
    return month


def event_create(request):
    instance = Event()
    data = request.POST.copy()
    data["author"] = request.user
    form = EventForm(data or None, instance=instance)
    if request.POST:
        if form.is_valid():  # pragma: no cover
            form.save()  # pragma: no cover
            return HttpResponseRedirect(reverse("cal:calendar"))  # pragma: no cover
        else:  # pragma: no cover
            # If the text fields are empty AND the time is invalid
            date_time_obj = datetime.strptime(data["start_time"], '%Y-%m-%dT%H:%M')
            if (data["title"] == "" or data["description"] == "") and (
                data["start_time"] > data["end_time"]
            ):
                messages.info(
                    request,
                    "Must have title, description, and start time before end time.",
                )

            # If the text fields are empty BUT the time is VALID
            elif (data["title"] == "" or data["description"] == "") and (
                data["start_time"] < data["end_time"]
            ):
                messages.info(request, "Must have title and description.")

            # If the time is INVALID
            elif data["start_time"] > data["end_time"]:
                messages.info(
                    request, "Start time must be before end time."
                )  # pragma: no cover
            elif date_time_obj<datetime.now():
                 messages.info(
                    request, "Events cannot be created in the past."
                )
            # If TIME fields are EMPTY
            elif data["start_time"] == "" or data["end_time"] == "":
                if data["title"] == "" or data["description"] == "":
                    messages.info(request, "All fields required.")
                else:
                    messages.info(request, "Must select both start and end time.")

    return render(request, "cal/create_event.html", {"event": form})  # pragma: no cover


def event_view(request, pk):
    instance = get_object_or_404(Event, pk=pk)
    form = EventForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("cal:calendar"))  # pragma: no cover
    return render(request, "cal/view_event.html", {"event": form})  # pragma: no cover


def event_update(request, pk):
    instance = get_object_or_404(Event, pk=pk)
    form = EventForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("cal:calendar"))
    return render(request, "cal/update_event.html", {"event": form})


def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventForm(request.POST or None, instance=event)
    if request.method == "POST":
        event.delete()
        return HttpResponseRedirect(reverse("cal:calendar"))  # pragma: no cover
    return render(request, "cal/delete_event.html", {"event": form})  # pragma: no cover
