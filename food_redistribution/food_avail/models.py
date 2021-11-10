from django.db import models
from django.urls import reverse
from accounts.models import User


class Food_Avail(models.Model):
    food_available = models.IntegerField()
    description = models.TextField(blank=True)
    available_till = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)