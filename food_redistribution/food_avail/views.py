from django.shortcuts import render
from .models import *
from .forms import FoodAvailForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
# Create your views here.


def check_existing_post(request):
    data = request.POST.copy()
    data["author"] = request.user
    if len(Food_Avail.objects.filter(author=request.user)) > 0:
        return False
    else:
        return True


def post_available_food(request):
    instance = Food_Avail()
    data = request.POST.copy()
    data["author"] = request.user
    form = FoodAvailForm(data or None, instance=instance)
    if request.POST and form.is_valid() and check_existing_post(request):
        form.save()
        return HttpResponseRedirect(reverse("accounts:home"))
    else:
        messages.info(
            request, "food availability by restaurant has already been posted!"
        )
    return render(request, "food_avail/post_food_avail.html", {"food": form})


def check_food_availibility(request):
    food = Food_Avail.objects.all()
    return render(request, "food_avail/view_food_avail.html", {"food": food})
