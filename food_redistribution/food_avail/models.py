from django.db import models
from accounts.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from datetime import datetime
import pytz


class FoodAvail(models.Model):
    def present_or_future_date(value):
        eastern = pytz.timezone("US/Eastern")
        if value < eastern.localize(datetime.now()):
            raise ValidationError("The date cannot be in the past!")
        return value

    food_available = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    description = models.TextField(blank=True)
    available_till = models.DateTimeField(validators=[present_or_future_date])
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    def allow_only_one_instance(self, instance):
        if len(FoodAvail.objects.filter(author=instance.author)) > 0:
            raise ValidationError("User has already created food availibility post!")
