from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Name(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.user


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    time = models.TimeField()
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.user)
