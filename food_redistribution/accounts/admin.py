
from django.contrib import admin

# Register your models here.
from .models import FoodRedistributor, Post, Restaurant

admin.site.register(FoodRedistributor)
admin.site.register(Restaurant)
admin.site.register(Post)

