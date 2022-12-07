from django.views.generic import TemplateView, FormView
from datetime import datetime, timezone
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from .models import Booking
from .forms import DateForm

def booking(request):
    #Calls allowedday function to show next two weeks of days
    days = allowedDay(15)

    #Allows user to see unbooked days
    availableDays = dayValidCheck(days)


    if request.method == 'POST':
        advice = request.POST.get('advice')
        choice = request.POST.get('choice')
        date = request.POST.get('date')



class HomeView(TemplateView):
    template_name = 'base.html'


class FormView(FormView):
    form_class = DateForm
    template_name = 'index.html'
