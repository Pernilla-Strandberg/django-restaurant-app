from django.urls import include, path

from . import views
from .views import (
    BookingCreateView,
    BookingDeleteView,
    BookingDetailView,
    BookingListView,
    BookingUpdateView,
)

urlpatterns = [

    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    # booking overview
    path('my-bookings/', BookingListView.as_view(), name='booking_list'),
    # booking details
    path('my-bookings/<int:pk>', BookingDetailView.as_view(), name='booking_detail'),
    # booking create, edit, delete
    path('my-bookings/new/', BookingCreateView.as_view(), name='booking_create'),
    path('my-bookings/edit/<int:pk>/', BookingUpdateView.as_view(), name='booking_edit'),
    path('my-bookings/delete/<int:pk>/', BookingDeleteView.as_view(), name='booking_delete'),
]