from django import forms
from django.contrib.admin import widgets
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking

        fields = ['name', 'date']
