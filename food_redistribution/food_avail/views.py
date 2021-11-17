from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import FoodAvailForm
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
            return HttpResponseRedirect(reverse("accounts:home"))
    else:
        instance = get_object_or_404(FoodAvail, author=request.user)
        form = FoodAvailForm(request.POST, request.FILES, instance=instance)
        if request.method == "POST":
            form = FoodAvailForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("accounts:home"))
        else:
            form = FoodAvailForm(instance=instance)
    return render(request, "food_avail/post_food_avail.html", {"food": form})


def check_food_availibility(request):
    food = FoodAvail.objects.all()
    return render(request, "food_avail/view_food_avail.html", {"food": food})
