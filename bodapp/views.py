from django.views.generic import TemplateView, FormView
from datetime import datetime, timezone
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from .models import Booking
from .forms import DateForm

def index(request):
    return render(request, "index.html",{})

def booking(request):
    daysfor = daysFor(15)

    availableDays = areDaysAvailable(daysfor)

    if request.method == 'POST':
        advice = request.POST.get('advice')
        choice = request.POST.get('choice')
        if advice == None:
            messages.success(request, "Select some Advice")
            return redirect('booking')

        if choice == None:
            messages.success(request, "Select a Choice")
            return redirect('booking')

    # Stored user choices in django
    request.session['advice'] = advice
    request.session['choice'] = choice
    request.session['date'] = date

    return redirect('finaliseBooking')



