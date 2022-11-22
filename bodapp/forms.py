from django import forms
from django.contrib.admin import widgets
from .models import Booking


class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
