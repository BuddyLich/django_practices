from django import forms
from . import models


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):

    class Meta:
        TIME_CHOICE = [
            ('900', '9:00'),
            ('930', '9:30'),
            ('1000', '10:00'),
            ('1030', '10:30'),
            ('1100', '11:00'),
            ('1130', '11:30'),
            ('1200', '12:00'),
            ('1230', '12:30'),
            ('1300', '13:00'),
            ('1300', '13:30'),
            ('1400', '14:00'),
            ('1400', '14:30'),
            ('1500', '15:00'),
            ('1530', '12:30'),
            ('1600', '16:00'),
            ('1630', '16:30'),
            ('1700', '17:00'),
            ('1730', '17:30'),
            ('1800', '18:00'),
        ]

        model = models.Booking
        fields = ['booking_date', 'booking_time',  'type', 'additional_massages']

        widgets = {
            'booking_date': DateInput,
            'booking_time': forms.Select(choices=TIME_CHOICE)
        }
