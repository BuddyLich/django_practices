from django import forms
from . import models


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):

    class Meta:
        TIME_CHOICE = [
            ('9:00', '9:00'),
            ('9:30', '9:30'),
            ('10:00', '10:00'),
            ('10:30', '10:30'),
            ('11:00', '11:00'),
            ('11:30', '11:30'),
            ('12:00', '12:00'),
            ('12:30', '12:30'),
            ('13:00', '13:00'),
            ('13:00', '13:30'),
            ('14:00', '14:00'),
            ('14:30', '14:30'),
            ('15:00', '15:00'),
            ('15:30', '12:30'),
            ('16:00', '16:00'),
            ('16:30', '16:30'),
            ('17:00', '17:00'),
            ('17:30', '17:30'),
            ('18:00', '18:00'),
        ]

        model = models.Booking
        fields = ['booking_date', 'booking_time',  'type', 'additional_massages']

        widgets = {
            'booking_date': DateInput,
            'booking_time': forms.Select(choices=TIME_CHOICE)
        }
