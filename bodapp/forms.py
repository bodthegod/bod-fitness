from django import forms
from django.contrib.admin import widgets
from .models import Booking


class DateForm(forms.ModelForm):
    """
    Form for datetime
    """
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    class Meta:
        model = Booking
        fields = ('date',)


class BookingForm(forms.ModelForm):
    """
    Form for all fields based on user
    """
    class Meta:
        model = Booking
        fields = ('user', 'advice', 'choice', 'date',)
