from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import FoodAvailForm, TimeSlotForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def check_existing_post(request):
    data = request.POST.copy()
    data["author"] = request.user
    if len(FoodAvail.objects.filter(author=request.user)) > 0:
        return True
    else:
        return False

def check_existing_timeslot(request):
    data = request.POST.copy()
    data["time_slot_owner"] = request.user
    if len(TimeSlot.objects.filter(time_slot_owner=request.user)) > 0:
        return True
    else:
        return False

def create_bookings(request):
    return render(request, "food_avail/bookings.html")


@login_required
def post_available_food(request):
    if not check_existing_post(request):
        instance = FoodAvail()
        data = request.POST.copy()
        data["author"] = request.user
        form = FoodAvailForm(data or None, instance=instance)
        if request.POST and form.is_valid():
            form.save()
            print("Working")
            return HttpResponseRedirect(reverse("accounts:home"))
    else:
        instance = get_object_or_404(FoodAvail, author=request.user)
        form = FoodAvailForm(request.POST, request.FILES, instance=instance)
        if request.method == "POST":
            form = FoodAvailForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                print("Working")
                return HttpResponseRedirect(reverse("food_avail:view_food_avail_res"))
                # return HttpResponseRedirect(reverse("accounts:home"))
        else:
            form = FoodAvailForm(instance=instance)
            print("not working")
    return render(request, "food_avail/post_food_avail.html", {"food": form})

@login_required
def view_available_food(request):
    instance = FoodAvail.objects.get(author=request.user)
    return render(request, "food_avail/view_food.html", {"food": instance})

def check_food_availibility(request):
    food = FoodAvail.objects.all()
    return render(request, "food_avail/view_food_avail.html", {"food": food})

@login_required
def create_timeslots(request):
    if not check_existing_timeslot(request):
        instance = TimeSlot()
        data = request.POST.copy()
        data["time_slot_owner"] = request.user
        data["food_avail_id"] = FoodAvail.objects.get(author=request.user)
        form = TimeSlotForm(data or None, instance=instance)
        if request.POST and form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("accounts:home"))
    else:
        instance = get_object_or_404(TimeSlot, time_slot_owner=request.user)
        form = TimeSlotForm(request.POST, request.FILES, instance=instance)
        if request.method == "POST":
            form = TimeSlotForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("accounts:home"))
        else:
            form = TimeSlotForm(instance=instance)
    return render(request, "food_avail/timeslots.html", {"timeslot": form})

