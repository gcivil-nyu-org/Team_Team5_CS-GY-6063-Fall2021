from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class FoodRedistributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="")
    # phone = models.CharField(max_length=200, null=True)
    # email = models.CharField(max_length=200, null=True)
    # date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="")
    # phone = models.CharField(max_length=200, null=True)
    # email = models.CharField(max_length=200, null=True)
    # date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name