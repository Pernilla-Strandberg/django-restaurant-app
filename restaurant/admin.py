from django.contrib import admin
from .models import BookingModel


# Register the Admin classes for BookingModel using the decorator
@admin.register(BookingModel)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('created_on', 'last_name', 'first_name', 'guests', 'day', 'time')
    list_filter = ('day', 'last_name', 'created_on')