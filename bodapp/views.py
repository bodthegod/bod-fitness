from django.views.generic import TemplateView, FormView
from django.shortcuts import render
from django.views import generic
from .forms import DateForm
# from .models import Booking, Name


class HomeView(TemplateView):
    template_name = 'base.html'


class FormView(FormView):
    form_class = DateForm
    template_name = 'index.html'
