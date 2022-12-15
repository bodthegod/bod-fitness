from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import TemplateView, FormView
from datetime import datetime, timedelta
from django.views import generic
from django.contrib import messages
from django.conf import settings
from .models import *
from .forms import BookingForm
from .contexts import *


# class HomeView(TemplateView):
# #    template_name = 'index.html'
# #def base(request):
# #    return render(request, 'bodfitness/base.html')


# #class FormView(FormView):
# #    template_name = 'booking.html'
def index(request):
    return render(request, 'index.html', {})


def booking(request):

    daysfor = daysFor(7)

    availableDays = areDaysAvailable(daysfor)

    if request.method == 'POST':
        advice = request.POST.get('advice')
        choice = request.POST.get('choice')
        date = request.POST.get('date')

        # Stored user choices in django
        request.session['advice'] = advice
        request.session['choice'] = choice
        request.session['date'] = date

        return redirect('finaliseBooking')

    return render(request, 'booking.html', {
            'daysfor': daysfor,
            'availableDays': availableDays,
        })


def finaliseBooking(request):
    today = datetime.now()
    user = request.user
    preDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=7)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    topDate = strdeltatime

    advice = request.session.get('advice')
    choice = request.session.get('choice')
    date = request.session.get('date')

    if request.method == 'POST':
        day = displayDay(date)
    if advice != None:
        if choice != None:
            if date <= topDate and date >= preDate:
                if Booking.objects.filter(date=date).count() < 1:
                    BookingForm = Booking.objects.get_or_create(
                        user = user,
                        advice = advice,
                        choice = choice,
                        date = date,
                    )
                    messages.success(request, "Booking Made!")
                    return redirect('index.html')
                else:
                    messages.success(request, "There are no more bookings available on this day.")
            else:
                messages.success(request, "This date is incorrect, please select a correct date.")
        else:
            messages.success(request, "Please select a choice.")
    else:
        messages.success(request, "Please select an advice topic.")

    return render(request, 'finalisebooking.html', {})


def displayDay(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y


def daysFor(days):
    today = datetime.now()
    daysfor = []
    for i in range(0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Tuesday' or y == 'Wednesday':
            daysfor.append(x.strftime('%Y-%m-%d'))
    return daysfor


def areDaysAvailable(x):
    availableDays = []
    for d in x:
        if Booking.objects.filter(date=d).count() < 1:
            availableDays.append(d)
    return availableDays
