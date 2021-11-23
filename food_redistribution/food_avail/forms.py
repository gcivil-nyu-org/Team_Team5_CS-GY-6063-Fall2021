from django import forms
from django.forms import DateInput, ModelForm, TextInput

from food_avail.models import FoodAvail, TimeSlot

class FoodAvailForm(ModelForm):
    class Meta:
        model = FoodAvail
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
            "food_available": forms.NumberInput(
                attrs={"placeholder": "Food Available"}
            ),
            "description": TextInput(attrs={"placeholder": "Description"}),
            "author": forms.HiddenInput(),
        }
        fields = ["food_available", "description", "author"]

        def __init__(self, *args, **kwargs):
            super(FoodAvailForm, self).__init__(*args, **kwargs)
            # input_formats parses HTML5 datetime-local input to datetime field
            self.fields["available_till"].input_formats = ("%Y-%m-%dT%H:%M",)


class TimeSlotForm(ModelForm):
    class Meta:
        model = TimeSlot
        widgets = {
            "time_slot_owner": forms.HiddenInput(),
            "start_time": DateInput(attrs={"type": "time"}, format="%H:%M"),
            "end_time": DateInput(attrs={"type": "time"}, format="%H:%M"),
        }
        fields = ["start_time", "end_time", "time_slot_owner"]

    def clean(self):
        start_time = self.cleaned_data.get("start_time")
        end_time = self.cleaned_data.get("end_time")

        print(start_time)
        print
        if start_time and end_time:
            if start_time > end_time:
                # raise forms.ValidationError("Start time cannot be greater than end time")
                self.add_error(  # pragma: no cover
                    "start_time", "start time cannot be greater than end time!"
                )
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(TimeSlotForm, self).__init__(*args, **kwargs)
        # input_formats parses HTML5 datetime-local input to datetime field
        self.fields["start_time"].input_formats = ("%H:%M",)
        self.fields["end_time"].input_formats = ("%H:%M",)
