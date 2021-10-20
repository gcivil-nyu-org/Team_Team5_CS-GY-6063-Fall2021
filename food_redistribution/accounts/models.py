from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class FoodRedistributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="")
    name_of_food_redis = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="")
    name_of_restaurant = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
