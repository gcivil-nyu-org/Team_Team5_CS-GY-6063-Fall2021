from django.db import models
from django.urls import reverse
from accounts.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)

    @property
    def get_html_url(self):
        url = reverse("cal:event_view", args=(self.id,))
        return f'<a href="{url}"> {self.name} </a>'

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=200, default='event')
    
    @property
    def get_html_url(self):
        url = reverse("cal:event_view", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
