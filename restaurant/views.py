from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import BookingModel
from .forms import BookingModelForm

# Create your views here.
def index(request):
    return render(request, "index.html",{})

class BookingListView(LoginRequiredMixin, ListView):
    """List bookings to current user"""
    model = BookingModel
    template_name = 'booking_overview.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        # Filter bookings based on current user
        return (
            BookingModel.objects.filter(user=self.request.user)
        )

class BookingDetailView(LoginRequiredMixin, DetailView):
    """View specific booking"""
    model = BookingModel
    template_name = 'booking.html'
    context_object_name = 'booking'

    def get_queryset(self):
        # Filter booking based on current user
        return (
            BookingModel.objects.filter(user=self.request.user)
        )

class BookingCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    List all objects from BookingModel, create object/objects in database and
    add success message to template.
    """
    model = BookingModel
    form_class = BookingModelForm
    template_name = 'booking_form.html'
    success_message = "Your booking is registered"

    def form_valid(self, form):
        # Set the logged-in user before saving the form
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the detail view of the created object
        return reverse_lazy('booking_detail', kwargs={'pk': self.object.pk})

class BookingUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    List all objects from BookingModel, update object/objects in database and
    add success message to template.
    """
    model = BookingModel
    form_class = BookingModelForm
    template_name = 'booking_form_update.html'
    success_message = "Your booking was updated successfully"

    def get_object(self, queryset=None):
        # Ensure that the booking is fetched based on the user and the provided pk
        return get_object_or_404(BookingModel, user=self.request.user, pk=self.kwargs['pk'])

    def get_success_url(self):
        # Redirect to the detail view of the updated object
        return reverse_lazy('booking_detail', kwargs={'pk': self.object.pk})

class BookingDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Booking form delete view"""
    model = BookingModel
    template_name = 'booking_confirm_delete.html'

    def get_object(self, queryset=None):
        # Ensure that the booking is fetched based on the user and the provided pk
        return BookingModel.objects.filter(user=self.request.user, pk=self.kwargs['pk']).first()

    def get_success_url(self):
        # Specify the URL where the view should redirect after deletion
        return reverse_lazy('booking_list')

    def delete(self, request, *args, **kwargs):
        # Override the delete method to perform the deletion of the booking
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, "Booking deleted successfully")
        return redirect(success_url)
