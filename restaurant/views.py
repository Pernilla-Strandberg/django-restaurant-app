from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from .models import BookingModel

# Create your views here.
def index(request):
    return render(request, "index.html",{})

class BookingView(LoginRequiredMixin,generic.ListView):
    """List bookings to current user"""
    model = BookingModel
    template_name = 'booking_overview.html'

    def get_queryset(self):
        return (
            BookingModel.objects.filter(customer=self.request.user)
            .order_by('day')
        )