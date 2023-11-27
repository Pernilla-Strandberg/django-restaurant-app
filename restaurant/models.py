from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BookingModel(models.Model):

    # Fields
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customer_bookings"
    )
    # FK used because a booking can only have one customer but multiple
    # bookings can have the same customer

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    day = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    TOTAL_GUESTS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('10+C', '10+ - Contact Me'),
    )

    guests = models.CharField(
        max_length=4,
        choices=TOTAL_GUESTS,
        blank=True,
        default='2',
        help_text='Select number of guests',
    )

    # Metadata
    class Meta:
        ordering = ['day', 'time']

    # Methods
    def __str__(self):
        """String for representing the model object (in Admin site etc.)."""
        return f'{self.first_name}, {self.last_name}, {self.guests}, {self.day}, {self.time}, {self.created_on}'