from django.db import models
from django.contrib.auth.models import AbstractUser
from booking.models import Booking


class Users(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_barber = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
    gender = models.CharField(max_length=32)
    mobile_number = models.CharField(max_length=10, default='')
    bookings = models.ForeignKey(Booking, on_delete=models.CASCADE)
    blocked = models.BooleanField('Blocked', default=False)
    activated = models.BooleanField('Activated', default=False)


class Barber(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
