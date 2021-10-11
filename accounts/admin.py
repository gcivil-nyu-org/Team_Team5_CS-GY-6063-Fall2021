
from django.contrib import admin

# Register your models here.
from .models import FoodRedistributor, Restaurant

admin.site.register(FoodRedistributor)
admin.site.register(Restaurant)

