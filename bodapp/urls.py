from django.urls import path
from bodapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking', views.booking, name='booking'),
    path('finalise_booking/<booking_number>',
         views.finalise_booking, name='finalise_booking'),
]