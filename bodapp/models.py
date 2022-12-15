from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# ADVICE_TOPIC = (
#     ("Weight Gain", "Weight Gain"),
#     ("Weight Loss", "Weight Loss"),
#     ("Endurance", "Endurance"),
#     ("Strength Gain", "Strength Gain"),
# )

# BOOKING_CHOICE = (
#     ("Online", "Online"),
#     ("In Person", "In Person"),
# )


class Booking(models.Model):
    booking_number = models.CharField(
        max_length=32, null=False, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)

    def _generate_booking_number(self):
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        if not self.booking_number:
            self.booking_number = self._generate_booking_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} | date {self.date}"
        return self.booking_number
