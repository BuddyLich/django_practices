from django import forms
from .models import Booking
from datetime import datetime


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

        model = Booking
        fields = ['booking_date', 'booking_time',  'type', 'additional_massages']

        widgets = {
            'booking_date': DateInput,
            'booking_time': forms.Select(choices=TIME_CHOICE)
        }

    def clean(self):
        cleaned_data = super(BookingForm, self).clean()
        booking_date = cleaned_data.get('booking_date')
        booking_time = cleaned_data.get('booking_time')

        if "booking_date" in self.changed_data:
            dates_ahead = (booking_date - datetime.now().date()).days
            if dates_ahead < 0:
                raise forms.ValidationError("Booking date cannot earlier than today.")

            if dates_ahead > 15:
                raise forms.ValidationError("Booking date cannot later than 15 days.")

        if "booking_time" in self.changed_data:
            bookings_at_that_time = Booking.objects.filter(
                booking_date=booking_date,
                booking_time=booking_time,
                status__in=['pending', 'confirmed']
            ).all()

            if bookings_at_that_time.count() > (3 - 1):
                raise forms.ValidationError("Booking time already occupied.")

        return cleaned_data
