import pytest
from django.contrib.auth.models import User
from restaurant.forms import BookingModelForm

@pytest.fixture
def user():
    return User.objects.create_user(username="testuser", password="testpass")

@pytest.fixture
def valid_booking_data(user):
    return {
        'user': user,
        'first_name': 'Pernilla',
        'last_name': 'Strandberg',
        'email': 'pernillastrandberg87@example.com',
        'day': '2023-12-15',
        'time': '6 PM',
        'guests': '4',
    }
    
@pytest.mark.django_db
def test_booking_form_valid(valid_booking_data):
    form = BookingModelForm(data=valid_booking_data)
    assert form.is_valid()

@pytest.mark.django_db
def test_booking_form_invalid():
    # Test with invalid data
    invalid_data = {
        'user': None, 
        'first_name': '',
        'last_name': '',
        'email': 'invalid_email',
        'day': 'invalid_date',
        'time': 'invalid_time',
        'guests': 'invalid_guests',
    }
    form = BookingModelForm(data=invalid_data)
    assert not form.is_valid()