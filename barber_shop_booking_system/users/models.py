from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_customer = models.BooleanField(default=False)
    is_barber = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class CustomerInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='customer_id')
    mobile_number = models.CharField(max_length=10, default='')

    blocked = models.BooleanField('Blocked', default=False)
    activated = models.BooleanField('Activated', default=False)

    def __str__(self):
        return self.user.username


class BarberInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username
