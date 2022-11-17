from django.db import models
from django.contrib.auth.models import User


class Name(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.user


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=200)
    time = models.TimeField()

    def __str__(self):
        return str(self.user)
