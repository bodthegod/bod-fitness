from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import TemplateView, FormView
from datetime import datetime, timedelta
from django.views import generic
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import BookingForm
from .contexts import *


def index(request):
    """
    Renders landing page
    """
    return render(request, 'landing.html', {})


@login_required
def booking(request):
    """
    Function for booking
    """
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

    if request.method == 'POST':
        day = display_day(date)

        if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday':
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
                        return redirect(reverse('finalise_booking',
                                                args=[booking.booking_number]))
                else:
                    messages.success(
                        request,
                        "There are no more bookings available on this day.")
            else:
                messages.success(
                    request,
                    "This date is incorrect, please select a correct date.")
        else:
            messages.error(request, 'This date is incorrect')

    daysfor = days_for(7)
    available_days = are_days_available(daysfor)

    booking_available = False if available_days is None or len(
        available_days) == 0 else True

    return render(request, 'booking/booking.html', {'daysfor': daysfor,
                                                    'available_days':
                                                    available_days,
                                                    'booking_available':
                                                    booking_available, })


def finalise_booking(request, booking_number):
    """
    Finalise booking function
    """

    booking = get_object_or_404(Booking, booking_number=booking_number)
    context = {
        'booking': booking,
    }

    return render(request, 'booking/finalisebooking.html', context)


def account_panel(request):
    """
    Show only user specific bookings
    """
    if request.user.is_authenticated:
        bookings = Booking.objects.all()

    user = request.user
    bookings = Booking.objects.filter(user=user)
    past_bookings = []
    upcoming_bookings = []
    bookings_today = []

    for booking in bookings:
        if booking.date < datetime.today().date():
            if booking not in past_bookings:
                past_bookings.append(booking)
        elif booking.date > datetime.today().date():
            if booking not in upcoming_bookings:
                upcoming_bookings.append(booking)

    for booking in bookings:
        if booking.date == datetime.today().date():
            if booking not in bookings_today:
                bookings_today.append(booking)

    template = 'booking/userbookingsview.html'
    context = {
        "bookings": bookings,
        "past_bookings": past_bookings,
        "upcoming_bookings": upcoming_bookings,
        "bookings_today": bookings_today,
        'user': user,
    }

    return render(request, template, context)


@login_required
def created_bookings(request):
    """
    Page to view bookings
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have access to this \
            part of the site.")
        return redirect(reverse('index'))
    if request.user.is_authenticated:
        bookings = Booking.objects.all()

    past_bookings = []
    upcoming_bookings = []
    bookings_today = []

    for booking in bookings:
        if booking.date < datetime.today().date():
            if booking not in past_bookings:
                past_bookings.append(booking)
        elif booking.date > datetime.today().date():
            if booking not in upcoming_bookings:
                upcoming_bookings.append(booking)

    for booking in bookings:
        if booking.date == datetime.today().date():
            if booking not in bookings_today:
                bookings_today.append(booking)

    template = 'booking/createdbookings.html'
    context = {
        "bookings": bookings,
        "past_bookings": past_bookings,
        "upcoming_bookings": upcoming_bookings,
        "bookings_today": bookings_today,
    }

    return render(request, template, context)


@login_required
def booking_detail(request, booking_number):
    """
    Shows booking details
    """
    if request.user.is_authenticated:
        booking = get_object_or_404(Booking,
                                    booking_number=booking_number)

    template = 'booking/finalisebooking.html'
    context = {
        'booking': booking,
        'admin': True,
    }
    return render(request, template, context)


@login_required
def delete_booking(request, booking_number):
    """
    Allows for booking deletion
    """
    booking = get_object_or_404(Booking,
                                booking_number=booking_number)
    booking.delete()
    messages.info(request, f'Booking with booking number {booking_number}\
         has been successfully deleted.')
    return redirect('account_panel')


def display_day(x):
    """
    Function to return string of datetime
    """
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y


def days_for(days):
    """
    Function to return the next mon, tues or wed within the next week
    """
    today = datetime.now()
    daysfor = []
    for i in range(0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Tuesday' or y == 'Wednesday':
            daysfor.append(x.strftime('%Y-%m-%d'))
    return daysfor


def are_days_available(x):
    """
    Checks if days are available for booking
    """
    available_days = []
    for d in x:
        if Booking.objects.filter(date=d).count() < 1:
            available_days.append(d)
    return available_days
