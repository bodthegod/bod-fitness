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
    WEIGHT_GAIN = 1
    WEIGHT_LOSS = 2
    ENDURANCE = 3
    STRENGTH_GAIN = 4

    ADVICE_CHOICE = (
        (WEIGHT_GAIN, ('Weight Gain')),
        (WEIGHT_LOSS, ('Weight Loss')),
        (ENDURANCE, ('Endurance')),
        (STRENGTH_GAIN, ('Strength Gain')),)
    advice = models.PositiveSmallIntegerField(
        choices=ADVICE_CHOICE,
        default=WEIGHT_GAIN,
    )

    ONLINE = 1
    IN_PERSON = 2

    BOOKING_CHOICE = (
        (ONLINE, ('Online')),
        (IN_PERSON, ('In Person')),
    )
    choice = models.PositiveSmallIntegerField(
        choices=BOOKING_CHOICE,
        default=ONLINE,
    )
    date = models.DateField(default=datetime.now)

    def _generate_booking_number(self):
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        if not self.booking_number:
            self.booking_number = self._generate_booking_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.booking_number
