# from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Restaurant, FoodRedistributor


class RestuarantUserForm(UserCreationForm):
    name_of_restaurant = forms.CharField(
        label="Name of Restaurant", min_length=2, max_length=50, required=True
    )
    username = forms.CharField(
        label="Username", min_length=2, max_length=50, required=True
    )
    email = forms.EmailField(label="Email", required=True)
    password1 = forms.CharField(
        label="Password",
        min_length=8,
        max_length=40,
        widget=forms.PasswordInput,
        required=True,
    )
    password2 = forms.CharField(
        label="Confirm Password",
        min_length=8,
        max_length=40,
        widget=forms.PasswordInput,
        required=True,
    )
    phone = forms.CharField(label="Phone", max_length=10, required=True)
    address = forms.CharField(
        label="Address", min_length=2, max_length=50, required=True
    )

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        holder = User.objects.filter(email=email)
        if holder.count():
            print(email, "going into if")  # pragma: no cover
            raise ValidationError("Email already exists")
        return email

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    field_order = [
        "name_of_restaurant",
        "email",
        "username",
        "phone",
        "address",
        "password1",
        "password2",
    ]


class FoodRedistributorUserForm(UserCreationForm):
    name_of_food_redis = forms.CharField(
        label="Name of Food Redistributor", min_length=2, max_length=50, required=True
    )
    username = forms.CharField(
        label="Username", min_length=2, max_length=50, required=True
    )
    email = forms.EmailField(label="Email", required=True)
    password1 = forms.CharField(
        label="Password",
        min_length=8,
        max_length=40,
        widget=forms.PasswordInput,
        required=True,
    )
    password2 = forms.CharField(
        label="Confirm Password",
        min_length=8,
        max_length=40,
        widget=forms.PasswordInput,
        required=True,
    )
    phone = forms.CharField(label="Phone", max_length=10, required=True)
    address = forms.CharField(
        label="Address", min_length=2, max_length=50, required=True
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    # field_order = ["name_of_food_redis", "email",
    #               "username", "password1", "password2"]

    field_order = [
        "name_of_food_redis",
        "email",
        "username",
        "phone",
        "address",
        "password1",
        "password2",
    ]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            # "author": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }
        fields = ["title", "body", "pic"]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
        ]


class RestaurantUpdateForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        # fields = [
        #     "name_of_restaurant",
        #     "email",
        #     "phone",
        #     "address",
        # ]
        fields = [
            "name_of_restaurant",
            "phone",
            "address",
            "about",
            "profile_pic",
        ]


class FoodRedistributorUpdateForm(forms.ModelForm):
    class Meta:
        model = FoodRedistributor
        # fields = [
        #     "name_of_food_redis",
        #     "email",
        #     "phone",
        #     "address",
        # ]
        fields = [
            "name_of_food_redis",
            "phone",
            "address",
            "about",
            "profile_pic",
        ]


# class RestaurantUpdateForm(forms.ModelForm):
#     # Keep configuration in one place
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.form_show_labels = False

#     class Meta:
#         model = Restaurant
#         fields = ["name_of_restaurant", "email"]


# class FoodRedisUpdateForm(forms.ModelForm):
#     # Keep configuration in one place
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.form_show_labels = False

#     class Meta:
#         model = FoodRedistributor
#         fields = ["name_of_food_redis", "email"]
