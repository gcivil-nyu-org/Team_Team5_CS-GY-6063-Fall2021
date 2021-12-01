from django.db import models
from accounts.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from datetime import datetime
import pytz


class FoodAvail(models.Model):
    def present_or_future_date(value):
        eastern = pytz.timezone("US/Eastern")  # pragma: no cover
        if value < eastern.localize(datetime.now()):  # pragma: no cover
            raise ValidationError("The date cannot be in the past!")  # pragma: no cover
        return value  # pragma: no cover

    food_available = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class TimeSlot(models.Model):
    time_slot_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.start_time) + "-" + str(self.end_time)


class Booking(models.Model):
    bookings_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    meals_booked = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    start_time = models.TimeField()
    end_time = models.TimeField()
    restaurant = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="restaurant"
    )
