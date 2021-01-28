from django.db import models
from django.utils import timezone


class Booking(models.Model):
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=32, default='')
    additional_massages = models.TextField(max_length=256, default="")
