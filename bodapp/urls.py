from django.urls import path
from bodapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('booking', views.booking, name='booking'),
    path('finalise_booking/<booking_number>',
         views.finalise_booking, name='finalise_booking'),
    path('created_bookings',
         views.created_bookings, name='created_bookings'),
    path('booking_detail/<booking_number>',
         views.booking_detail, name='booking_detail'),
    path('delete_booking/<booking_number>',
         views.delete_booking, name='delete_booking'),
    path('account_panel', views.account_panel, name='account_panel'),

]
