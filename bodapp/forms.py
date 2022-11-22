from django import forms
from django.contrib.admin import widgets
from .models import Booking


class DateForm(forms.ModelForm):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    class Meta:
        model = Booking
        fields = ('name', 'date')
