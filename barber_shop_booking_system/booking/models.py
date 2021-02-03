from django.db import models
from django.utils import timezone
from users.models import CustomerInfo
from django.urls import reverse


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

    def __str__(self):
        return f'{self.customer.username} - {str(self.date)}'

    def get_absolute_url(self):
        return reverse('booking_detail', kwargs={'pk': self.pk})

    # @property
    # def booking_dt(self):
    #     return 0
