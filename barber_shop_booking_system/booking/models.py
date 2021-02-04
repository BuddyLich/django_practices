from django.db import models
from django.utils import timezone
from users.models import CustomerInfo
from django.urls import reverse
from datetime import datetime, timedelta


class Booking(models.Model):
    customer = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE, null=True)

    customer_name = models.CharField(max_length=32, default='')
    customer_mobile_number = models.CharField(max_length=10, default='')
    customer_email = models.CharField(max_length=64, default='')

    booking_date = models.DateField(default=timezone.now)
    booking_time = models.CharField(max_length=12, default='')

    type = models.CharField(max_length=32, default='')
    additional_massages = models.TextField(max_length=256, default="")
    is_online_booking = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.customer.user.username} - {str(self.booking_date)}'

    def get_absolute_url(self):
        return reverse('booking_detail', kwargs={'pk': self.pk})

    @property
    def booking_dt(self):
        dt = f"{str(self.booking_date)} {self.booking_time}"
        return datetime.strptime(dt, "%Y-%m-%d %H:%M")
    # probably a bad practice here, will be changed later
