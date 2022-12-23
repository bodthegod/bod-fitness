from django.contrib import admin
from .models import *


class BookingAdmin(admin.ModelAdmin):
    """
    Class for admin to see all fields for a user
    """

    readonly_fields = ('booking_number',)

    fields = ('user', 'advice', 'choice', 'date', 'booking_number')

    list_display = ('user', 'advice', 'choice', 'date', 'booking_number')

    ordering = ('-date',)


admin.site.register(Booking, BookingAdmin)
