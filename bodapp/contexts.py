from .models import *


def booking_details(request):

    booking_req = request.session.get('booking_request', {})
    advice = booking_req["advice"]
    choice = booking_req["choice"]
    date = booking_req["date"]

    context = {
        'advice': advice,
        'choice': choice,
        'date': date,
    }

    return context
