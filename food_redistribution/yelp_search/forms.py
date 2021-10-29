from django import forms
from .models import Restaurant


class LocationForm(forms.Form):
    location = forms.CharField(widget=forms.TextInput, label="Search Location")
