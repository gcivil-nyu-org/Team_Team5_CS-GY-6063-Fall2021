from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import FoodAvailForm, TimeSlotForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import View
from django.contrib import messages
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




# @login_required
class FoodAvailCreateView(CreateView):
    model = FoodAvail
    template_name = "food_avail/post_food_avail.html"
    form_class = FoodAvailForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super(FoodAvailCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(FoodAvailCreateView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Food Availability Posted Successfully.')
        success_url = '/food_avail_res/'
        return success_url

    def get(self, *args, **kwargs):
     if len(self.model.objects.filter(author=self.request.user)) > 0:
        return redirect("food_avail:update_food_avail")
        # return HttpResponseRedirect(reverse("food_avail:update_food_avail"))
     else:
        return super().get(*args, **kwargs)       

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['food'] = FoodAvail.objects.filter(author=self.request.user)
        return context

# @login_required
# def post_available_food(request):
#     if not check_existing_post(request):
#         instance = FoodAvail()
#         data = request.POST.copy()
#         data["author"] = request.user
#         form = FoodAvailForm(data or None, instance=instance)
#         if request.POST and form.is_valid():
#             form.save()
#             print("Working")
#             return HttpResponseRedirect(reverse("accounts:home"))
#     else:
#         instance = get_object_or_404(FoodAvail, author=request.user)
#         form = FoodAvailForm(request.POST, request.FILES, instance=instance)
#         if request.method == "POST":
#             form = FoodAvailForm(request.POST or None, instance=instance)
#             if form.is_valid():
#                 form.save()
#                 print("Working")
#                 return HttpResponseRedirect(reverse("food_avail:view_food_avail_res"))
#                 # return HttpResponseRedirect(reverse("accounts:home"))
#         else:
#             form = FoodAvailForm(instance=instance)
#             print("not working")
#     return render(request, "food_avail/post_food_avail.html", {"food": form})

@login_required
def food_avail_update_view(request):
    instance = get_object_or_404(FoodAvail, author=request.user)
    form = FoodAvailForm(request.POST, request.FILES, instance=instance)
    if request.method == "POST":
        form = FoodAvailForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Food Availability Posted Successfully.')
            return HttpResponseRedirect(reverse("food_avail:view_food_avail_res"))
        else:
            form = FoodAvailForm(instance=instance)

    # print("not working")
    # food_avail = FoodAvail.objects.get(author=request.user)
    return render(request, "food_avail/update_food_avail.html", {'form': form, 'food': instance})
    

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
            return HttpResponseRedirect(request.path_info)
    else:
        instance = get_object_or_404(TimeSlot, time_slot_owner=request.user)
        form = TimeSlotForm(request.POST, request.FILES, instance=instance)
        if request.method == "POST":
            form = TimeSlotForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.path_info)
        else:
            form = TimeSlotForm(instance=instance)
    return render(request, "food_avail/view_food_avail.html", {"timeslot": form})

