from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Booking(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now)
