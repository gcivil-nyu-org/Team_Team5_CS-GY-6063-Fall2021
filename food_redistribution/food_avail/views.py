from django.shortcuts import render
from .models import *
from .forms import FoodAvailForm
from django.http import HttpResponseRedirect
# Create your views here.

def post_available_food(request):
    instance = Food_Avail()
    data = request.POST.copy()
    data["author"] = request.user
    form = FoodAvailForm(data or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("accounts:home"))
    return render(request, "food_avail/post_food_avail.html", {"food": form})