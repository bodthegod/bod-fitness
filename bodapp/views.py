from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import TemplateView, FormView
from datetime import datetime, timedelta
from django.views import generic
from django.contrib import messages
from django.conf import settings
from .models import *
from .forms import BookingForm
from .contexts import *


def index(request):
    return render(request, 'index.html', {})


def booking(request):
    if request.method == 'POST':
        advice = request.POST.get('advice')
        choice = request.POST.get('choice')
        date = request.POST.get('date')

        # Stored user choices in django
        request.session['advice'] = advice
        request.session['choice'] = choice
        request.session['date'] = date

    today = datetime.now()
    user = request.user
    preDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=7)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    topDate = strdeltatime

    # advice = request.session.get('advice')
    # choice = request.session.get('choice')
    # date = request.session.get('date')

    if request.method == 'POST':
        day = displayDay(date)

        if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday':
            # if advice != None:
            #     if choice != None:
            if date <= topDate and date >= preDate:
                if Booking.objects.filter(date=date).count() < 1:
                    print(request.POST.get('date'))
                    booking_data_submitted = {
                        "user": request.POST.get("user"),
                        "advice": request.POST.get('advice'),
                        "choice": request.POST.get('choice'),
                        "date": request.POST.get('date')
                    }
                    request.session['booking_request'] = booking_data_submitted
                    # BookingForm = Booking.objects.get_or_create(
                    #   booking_data_submitted,
                    # )
                    booking_data_submitted = {
                        "user": request.user,
                        "advice": request.POST.get('advice'),
                        "choice": request.POST.get('choice'),
                        "date": request.POST.get('date')
                    }

                    booking_form = BookingForm(booking_data_submitted)
                    if booking_form.is_valid():
                        booking = booking_form.save(commit=False)
                        booking.save()
                        messages.success(request, "Booking Made!")
                        return redirect(reverse('finalise_booking', args=[booking.booking_number]))
                else:
                    messages.success(
                        request, "There are no more bookings available on this day.")
            else:
                messages.success(
                    request, "This date is incorrect, please select a correct date.")
            #     else:
            #         messages.success(request, "Please select a choice.")
            # else:
            #     messages.success(request, "Please select an advice topic.")
        else:
            messages.error(request, 'This date is incorrect')

    daysfor = daysFor(7)
    availableDays = areDaysAvailable(daysfor)

    return render(request, 'booking/booking.html', {'daysfor': daysfor,
                                                    'availableDays': availableDays, })


def finalise_booking(request, booking_number):
    booking = get_object_or_404(Booking, booking_number=booking_number)
    context = {
        'booking': booking,
    }

    return render(request, 'booking/finalisebooking.html', context)


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
