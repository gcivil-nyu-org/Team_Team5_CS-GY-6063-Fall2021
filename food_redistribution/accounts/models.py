from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    
    is_restaurant = models.BooleanField(default=False)
    is_food_redistributor = models.BooleanField(default=False)
    is_individual = models.BooleanField(default=False)

class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)

class FoodRedistributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)

class Individual(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
  
    
