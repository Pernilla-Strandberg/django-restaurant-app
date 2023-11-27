from django.db import models

# Create your models here.

class BookingModel(models.Model):

    # Fields
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    guests = models.CharField(max_length=3)
    day = models.DateField(null=True, blank=True)
    time = models.CharField(max_length=100)

    # Metadata
    class Meta:
        ordering = ['first_name', 'last_name', 'guests', 'day', 'time']

    # Methods
    def __str__(self):
        """String for representing the model object (in Admin site etc.)."""
        return f'{self.first_name}, {self.last_name}, {self.guests}, {self.day}, {self.time}'
