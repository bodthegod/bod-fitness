from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from datetime import datetime, timezone, timedelta
from django.views import generic
from django.contrib import messages
from .models import *
from .forms import DateForm


def index(request):
    return render(request, "index.html", {})


def booking(request):
    daysfor = daysFor(15)

    availableDays = areDaysAvailable(daysfor)

    if request.method == 'POST':
        advice = request.POST.get('advice')
        choice = request.POST.get('choice')
        date = request.POST.get('date')
        if advice == None:
            messages.success(request, "Select some Advice")
            return redirect('booking_form')

        if choice == None:
            messages.success(request, "Select a Choice")
            return redirect('booking_form')

        # Stored user choices in django
        request.session['advice'] = advice
        request.session['choice'] = choice
        request.session['date'] = date

        return redirect('finaliseBooking')

    return render(request, 'index.html', {
            'daysfor': daysfor,
            'availabledays': availableDays,
        })


def finaliseBooking(request):
    today = datetime.now()
    user = request.user
    preDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=15)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    topDate = strdeltatime

    advice = request.session.get('advice')
    choice = request.session.get('choice')
    date = request.session.get('day')
