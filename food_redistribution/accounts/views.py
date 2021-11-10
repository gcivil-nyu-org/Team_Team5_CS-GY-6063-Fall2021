# from django.db.models import fields
from django.shortcuts import render, redirect
from django.http import HttpResponse

# from django.forms import inlineformset_factory
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404


# Create your views here.
from .models import *
from .forms import (
    RestuarantUserForm,
    FoodRedistributorUserForm,
    PostForm,
    UserUpdateForm,
    RestaurantUpdateForm,
    FoodRedistributorUpdateForm,
)


# @user_passes_test(res_check)
def register_restaurant(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = RestuarantUserForm(request.POST)
        if request.method == "POST":
            if form.is_valid():
                # WRITE TEST FROM HERE
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                user_profile = Restaurant(user=user)
                # name = form.cleaned_data.get("username")
                current_site = get_current_site(request)
                mail_subject = "Activate your account."
                message = render_to_string(
                    "accounts/acc_active_email.html",
                    {
                        "user": user,
                        "domain": current_site.domain,
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": account_activation_token.make_token(user),
                    },
                )
                user_profile.email = form.cleaned_data.get("email")
                user_profile.name = form.cleaned_data.get("username")
                user_profile.name_of_restaurant = form.cleaned_data.get(
                    "name_of_restaurant"
                )
                user_profile.phone = form.cleaned_data.get("phone")
                user_profile.address = form.cleaned_data.get("address")
                user_profile.is_res = True
                user_profile.save()
                email = EmailMessage(mail_subject, message, to=[user_profile.email])
                email.send()
                return HttpResponse(
                    "Please confirm your email address to complete the registration"
                )
                # TO HERE

        context = {"form": form}
        return render(request, "accounts/restuarant_register.html", context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse(
            "Thank you for your email confirmation. Now you can login your account."
        )
    else:
        return HttpResponse("Activation link is invalid!")


def register_foodredistributor(request):
    if request.user.is_authenticated and request.user.is_active:
        return redirect("home2")
    else:
        form = FoodRedistributorUserForm(request.POST)
        if request.method == "POST":
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                user_profile = FoodRedistributor(user=user)
                current_site = get_current_site(request)
                mail_subject = "Activate your account."
                message = render_to_string(
                    "accounts/acc_active_email.html",
                    {
                        "user": user,
                        "domain": current_site.domain,
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": account_activation_token.make_token(user),
                    },
                )
                user_profile.email = form.cleaned_data.get("email")
                user_profile.name = form.cleaned_data.get("username")
                user_profile.name_of_food_redis = form.cleaned_data.get(
                    "name_of_food_redis"
                )
                user_profile.phone = form.cleaned_data.get("phone")
                user_profile.address = form.cleaned_data.get("address")
                user_profile.is_food_redis = True
                user_profile.save()
                email = EmailMessage(mail_subject, message, to=[user_profile.email])
                email.send()
                return HttpResponse(
                    "Please confirm your email address to complete the registration"
                )

        context = {"form": form}
        return render(request, "accounts/food_redistributor_register.html", context)


class PostView(ListView):
    model = Post
    template_name = "accounts/blogposts/blogposts.html"
    ordering = ["-id"]


class DetailedblogView(DetailView):
    model = Post
    template_name = "accounts/blogposts/detailedblog.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "accounts/blogposts/addpost.html"
    # fields = "__all__"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(UpdateView):
    model = Post
    template_name = "accounts/blogposts/update_post.html"
    fields = ["title", "body"]


class DeletePostView(DeleteView):
    model = Post
    template_name = "accounts/blogposts/delete_post.html"
    success_url = reverse_lazy("posts")


def res_check(user):
    try:
        get_object_or_404(Restaurant, user=user)
    except:
        return False
    else:
        return True


def login_restuarant(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            # TEST FROM HERE
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None and res_check(user) is True:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, "Username or password is incorrect")

        context = {}
        # TO HERE
        return render(request, "accounts/restuarantlogin.html", context)


def login_foodredistributor(request):
    if request.user.is_authenticated:
        return redirect("home2")
    else:
        # TEST FROM HERE
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None and res_check(user) is False:
                login(request, user)
                return redirect("home2")
            else:
                messages.info(request, "Username or password is incorrect")
                # TO HERE
        context = {}
        return render(request, "accounts/foodredislogin.html", context)

@login_required
def profile_update(request):

    user_update_form = None
    entity_update_form = None
    user_profile = None
    if request.method == "POST":
        if res_check(request.user):
            user_profile = Restaurant.objects.get(user=request.user)
            user_update_form = UserUpdateForm(request.POST, instance=request.user)
            entity_update_form = RestaurantUpdateForm(
                request.POST, instance=user_profile
            )
            if user_update_form.is_valid() and entity_update_form.is_valid():
                user_update_form.save()
                entity_update_form.save()
                messages.success(request, f"Your account has been updated!")
                return redirect("home")

        else:
            user_profile = FoodRedistributor.objects.get(user=request.user)
            user_update_form = UserUpdateForm(request.POST, instance=request.user)
            entity_update_form = FoodRedistributorUpdateForm(
                request.POST, instance=user_profile
            )
            if user_update_form.is_valid() and entity_update_form.is_valid():
                user_update_form.save()
                entity_update_form.save()
                messages.success(request, f"Your account has been updated!")
                return redirect("home")

    else:
        if res_check(request.user):
            user_profile = Restaurant.objects.get(user=request.user)
            user_update_form = UserUpdateForm(instance=request.user)
            entity_update_form = RestaurantUpdateForm(instance=user_profile)

        else:
            user_profile = FoodRedistributor.objects.get(user=request.user)
            user_update_form = UserUpdateForm(instance=request.user)
            entity_update_form = FoodRedistributorUpdateForm(instance=user_profile)

    context = {"u_form": user_update_form, "r_form": entity_update_form}

    return render(request, "accounts/updateprofile.html", context)


def logout_restuarant(request):
    logout(request)
    return redirect("login")


def logout_foodredistributor(request):
    logout(request)
    return redirect("login2")


@login_required(login_url="login")
def home(request):
    return render(request, "accounts/dashboard.html")


@login_required(login_url="login2")
def home2(request):
    return render(request, "accounts/dashboard.html")


@login_required(login_url="profile")
def profile(request):
    return render(request, "accounts/profile-card.html")


def landing(request):
    return render(request, "accounts/landing_page.html")


def choose_login(request):
    return render(request, "accounts/chooselogin.html")


def about(request):
    return render(request, "accounts/about.html")
