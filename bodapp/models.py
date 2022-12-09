from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone

ADVICE_TOPIC = (
    ("Weight Gain", "Weight Gain"),
    ("Weight Loss", "Weight Loss"),
    ("Endurance", "Endurance"),
    ("Strength Gain", "Strength Gain"),
)

BOOKING_CHOICE = (
    ("Online", "Online"),
    ("In Person", "In Person"),
)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    advice = models.CharField(max_length=15, choices=ADVICE_TOPIC, default="Weight Gain")
    choice = models.CharField(max_length=15, choices=BOOKING_CHOICE, default="Online")
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return f"{self.user.username} | date {self.date}"
