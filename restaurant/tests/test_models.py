import pytest
from datetime import date, timedelta
from django.contrib.auth.models import User
from restaurant.models import BookingModel

@pytest.fixture
def user():
    return User.objects.create_user(username="testuser", password="testpass")

def test_create_booking(user):
    # Create a booking and ensure fields are correctly set
    booking = BookingModel.objects.create(
        user=user,
        first_name="Pernilla",
        last_name="Strandberg",
        email="pernillastrandberg87@example.com",
        day="2023-12-14",
        time="4 PM",
        guests="2",
    )
    assert booking.user == user
    assert booking.first_name == "Pernilla"
    assert booking.last_name == "Strandberg"
    assert booking.email == "pernillastrandberg87@example.com"
    assert booking.day == date(2023, 12, 14)
    assert booking.time == "4 PM"
    assert booking.guests == 2

@pytest.mark.django_db
def test_booking_model_str_method(user):
    # Test string representation of BookingModel instance
    booking = BookingModel.objects.create(
        user=user,
        first_name="Anna",
        last_name="Strandberg",
        email="annastrandberg@example.com",
        day="2023-12-13",
        time="6 PM",
        guests="4",
    )
    assert str(booking) == "Anna Strandberg - 2023-12-13 6 PM"

@pytest.mark.django_db
def test_booking_model_past_date(user):
    # Create booking yesterday and assert error validation
    yesterday = date.today() - timedelta(days=1)
    with pytest.raises(ValueError):
        BookingModel.objects.create(
            user=user,
            first_name="Karl",
            last_name="Larsson",
            email="karllarsson@example.com",
            day=yesterday,
            time="7 PM",
            guests="3",
        )
@pytest.mark.django_db
def test_booking_model_invalid_email(user):
    # Create booking with invalid email and assert ValueError raising
    with pytest.raises(ValueError):
        BookingModel.objects.create(
            user=user,
            first_name="Invalid",
            last_name="Email",
            email="invalid-email",  # Invalid email
            day="2023-12-15",
            time="12 PM",
            guests="5",
        )