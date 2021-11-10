from django import forms
from django.forms import DateInput, ModelForm, TextInput

from cal.models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
            "start_time": DateInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
            "end_time": DateInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
            "title": TextInput(attrs={"placeholder": "Title"}),
            "description": TextInput(attrs={"placeholder": "Description"}),
            "author":  forms.HiddenInput(),
        }
        fields = ["title", "description", "start_time", "end_time", "author"]

        def __init__(self, *args, **kwargs):
            super(EventForm, self).__init__(*args, **kwargs)
            # input_formats parses HTML5 datetime-local input to datetime field
            self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
            self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)
