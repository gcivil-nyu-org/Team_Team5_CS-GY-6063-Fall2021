from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import RestuarantUserForm, FoodRedistributorUserForm


def register_restaurant(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = RestuarantUserForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                user = form.save()
                #user = form.save(commit=False)
                #user.is_active = False
                # user.save()
                user_profile = Restaurant(user=user)
                name = form.cleaned_data.get('username')
                messages.success(
                    request, f'Success! Account created for {name}')
                user_profile.save()
                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/restuarant_register.html', context)


def register_foodredistributor(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = FoodRedistributorUserForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                user = form.save()
                #user = form.save(commit=False)
                #user.is_active = False
                # user.save()
                user_profile = FoodRedistributor(user=user)
                name = form.cleaned_data.get('username')
                messages.success(
                    request, f'Success! Account created for {name}')
                user_profile.save()
                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/food_redistributor_register.html', context)

# def registerPage(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	else:
# 		form = CreateUserForm()
# 		if request.method == 'POST':
# 			form = CreateUserForm(request.POST)
# 			if form.is_valid():
# 				form.save()
# 				user = form.cleaned_data.get('username')
# 				messages.success(request, 'Account was created for ' + user)

# 				return redirect('login')


# 		context = {'form':form}
# 		return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, username)
                messages.info(request, password)

                messages.info(request, 'Username OR Password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/dashboard.html')
