from django.contrib import admin
from .models import BookingModel


# Register the Admin classes for Booking using the decorator
@admin.register(BookingModel)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'guests', 'day', 'time')

    fields = ('last_name', 'first_name', 'guests', 'day', 'time')