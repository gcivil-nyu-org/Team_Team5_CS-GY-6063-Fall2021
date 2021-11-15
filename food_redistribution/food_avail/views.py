from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import FoodAvailForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def check_existing_post(request):
    data = request.POST.copy()
    data["author"] = request.user
    if len(Food_Avail.objects.filter(author=request.user)) > 0:
        return False
    else:
        return True


@login_required
def post_available_food(request):
    instance = get_object_or_404(Food_Avail, author=request.user)
    form = FoodAvailForm(request.POST, request.FILES, instance=instance)
    if request.method == 'POST':
        form = FoodAvailForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('accounts:home')
    else:
        form = FoodAvailForm(instance=instance)
    return render(request, 'food_avail/post_food_avail.html', {'food': form})

def check_food_availibility(request):
    food = Food_Avail.objects.all()
    return render(request, "food_avail/view_food_avail.html", {"food": food})
