from django.contrib import admin

from .models import BookingModel


# Register Admin classes for BookingModel using decorator
@admin.register(BookingModel)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("day", "last_name", "first_name", "guests", "time", "created_on")
    list_filter = ("day", "created_on")
