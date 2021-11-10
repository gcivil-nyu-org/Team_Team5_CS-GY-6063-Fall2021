from django import forms
from django.forms import DateInput, ModelForm, TextInput

from food_avail.models import Food_Avail


class FoodAvailForm(ModelForm):
    class Meta:
        model = Food_Avail
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
            "available_till": DateInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
            "food_available": forms.NumberInput(attrs={"placeholder": "Food Available"}),
            "description": TextInput(attrs={"placeholder": "Description"}),
            "author": forms.HiddenInput(),
        }
        fields = ["food_available", "available_till", "description", "author"]

        def __init__(self, *args, **kwargs):
            super(EventForm, self).__init__(*args, **kwargs)
            # input_formats parses HTML5 datetime-local input to datetime field
            self.fields["available_till"].input_formats = ("%Y-%m-%dT%H:%M",)
