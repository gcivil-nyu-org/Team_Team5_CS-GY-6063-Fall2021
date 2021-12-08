from django import forms
from django.forms import DateInput, ModelForm, TextInput
from datetime import datetime


from cal.models import Event

choices = [
    ("event", "event"),
    ("donation", "donation"),
    ("volunteer", "volunteer"),
    ("discount", "discount"),
    ("free", "free"),
]


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
            "author": forms.HiddenInput(),
            "category": forms.Select(choices=choices, attrs={"class": "form-control"}),
        }
        fields = [
            "title",
            "description",
            "start_time",
            "end_time",
            "author",
            "category",
        ]

    def clean(self):

        start_time = self.cleaned_data.get("start_time")
        end_time = self.cleaned_data.get("end_time")

        if start_time and end_time:
            if start_time > end_time:
                # raise forms.ValidationError("Start time cannot be greater than end time")
                self.add_error(  # pragma: no cover
                    "start_time", "start time cannot be greater than end time!"
                )
            try:
                start_time = start_time.strftime("%Y-%m-%d %H:%M:%S")
                if start_time < datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
                    self.add_error(  # pragma: no cover
                        "start_time", "start time cannot be in the past!"
                    )
            except Exception as e:
                print(e)

        return self.cleaned_data

        def __init__(self, *args, **kwargs):
            super(EventForm, self).__init__(*args, **kwargs)
            # input_formats parses HTML5 datetime-local input to datetime field
            self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
            self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)
