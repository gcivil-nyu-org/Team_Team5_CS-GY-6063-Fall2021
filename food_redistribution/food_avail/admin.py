from django.contrib import admin
from .models import FoodAvail, TimeSlot, Booking

# Register your models here.
admin.site.register(FoodAvail)
admin.site.register(TimeSlot)
admin.site.register(Booking)
