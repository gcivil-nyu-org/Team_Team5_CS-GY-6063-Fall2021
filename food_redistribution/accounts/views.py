from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


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
                # user = form.save()
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                user_profile = Restaurant(user=user)
                name = form.cleaned_data.get('username')
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('accounts/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                # form.clean_email()
                user_profile.email = to_email
                nameofres = form.cleaned_data.get('name_of_restaurant')
                user_profile.name = name
                user_profile.name_of_restaurant = nameofres
                phone_r = form.cleaned_data.get('phone')
                user_profile.phone = phone_r
                address_r = form.cleaned_data.get('address')
                user_profile.address = address_r
                user_profile.save()
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                return HttpResponse('Please confirm your email address to complete the registration')
                # messages.success(
                #     request, f'Success! Account created for {name}')
                # user_profile.save()
                # return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/restuarant_register.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def register_foodredistributor(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = FoodRedistributorUserForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                # user = form.save()
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                user_profile = FoodRedistributor(user=user)
                name = form.cleaned_data.get('username')
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('accounts/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                user_profile.email = to_email
                nameofredis = form.cleaned_data.get('name_of_food_redis')
                user_profile.name = name
                user_profile.name_of_food_redis = nameofredis
                phone_r = form.cleaned_data.get('phone')
                user_profile.phone = phone_r
                address_r = form.cleaned_data.get('address')
                user_profile.address = address_r
                user_profile.save()
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                return HttpResponse('Please confirm your email address to complete the registration')
                # messages.success(
                #     request, f'Success! Account created for {name}')
                # user_profile.save()
                # return redirect('login2')

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

def login_restuarant(request):
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
                messages.info(request, 'Username OR Password is incorrect')

        context = {}
        return render(request, 'accounts/restuarantlogin.html', context)


def login_foodredistributor(request):
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
                messages.info(request, 'Username OR Password is incorrect')

        context = {}
        return render(request, 'accounts/foodredislogin.html', context)


def logout_restuarant(request):
    logout(request)
    return redirect('login')


def logout_foodredistributor(request):
    logout(request)
    return redirect('login2')


@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/dashboard.html')


@login_required(login_url='login2')
def home(request):
    return render(request, 'accounts/dashboard.html')


@login_required(login_url='profile')
def profile(request):
    return render(request, 'accounts/profile-card.html')
