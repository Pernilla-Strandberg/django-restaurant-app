from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date


def validate_email(value):
        """Email validation"""
        validator = EmailValidator("Enter a valid email address.")
        validator(value)

class BookingModel(models.Model):
    # Fields
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_bookings", default=1
    )
    # FK used because a booking can only have one user but multiple
    # bookings can have the same user

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(validators=[validate_email])
    day = models.DateField("Visiting date")

    TIME = (
        ("6 PM", "6 PM"),
        ("7 PM", "7 PM"),
        ("8 PM", "8 PM"),
        ("9 PM", "9 PM"),
        ("10 PM", "10 PM"),
    )

    time = models.CharField(max_length=10, choices=TIME, default="6 PM")
    created_on = models.DateTimeField(auto_now_add=True)

    TOTAL_GUESTS = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("10+C", "10+ - Contact Me"),
    )

    guests = models.CharField(
        max_length=4,
        choices=TOTAL_GUESTS,
        default="2",
        help_text="Select number of guests",
    )

    # Metadata
    class Meta:
        ordering = ["day", "time"]
        verbose_name = "Booking"

    # Methods
    def __str__(self):
        """String to represent the model object"""
        return f"{self.first_name} {self.last_name}, {self.day} at {self.time}"

    def get_absolute_url(self):
        # Return reverse('booking_list', args=(str(self.id)))
        return reverse("author-detail", kwargs={"pk": self.pk})

    def clean(self):
        # Ensure booking date is not in the past
        if self.day < date.today():
            raise ValidationError("You cannot book a table in the past.")

    def save(self, *args, **kwargs):
        self.clean()  # Clean validation before saving
        super().save(*args, **kwargs)