from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_barber = models.BooleanField(default=False)


class CustomerInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='customer_id')
    mobile_number = models.CharField(max_length=10, default='')
    email = models.EmailField(max_length=64, default='')

    blocked = models.BooleanField('Blocked', default=False)
    activated = models.BooleanField('Activated', default=False)


class BarberInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
