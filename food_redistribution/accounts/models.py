from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class FoodRedistributor(models.Model):
    user = models.OneToOneField(
        User, related_name="foodredis", null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="")
    name_of_food_redis = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)
    is_food_redis = models.BooleanField(default=False)
    about = models.TextField(max_length=500, default="Add a description here!")
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="images/profile/")

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    user = models.OneToOneField(
        User, related_name="rest", null=True, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, default="")
    name_of_restaurant = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)
    is_res = models.BooleanField(default=False)
    about = models.TextField(max_length=500, default="Add a description here!")
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="images/profile/")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    pic = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + "|" + str(self.author)

    def get_absolute_url(self):
        return reverse("accounts:blog-details", args=(str(self.id)))
