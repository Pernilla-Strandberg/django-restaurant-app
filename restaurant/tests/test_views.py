import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from restaurant.models import BookingModel
from django.test import Client

@pytest.fixture
def user():
    return User.objects.create_user(username="testuser", password="testpass")

@pytest.fixture
def booking(user):
    return BookingModel.objects.create(
        user=user,
        first_name="Pernilla",
        last_name="Strandberg",
        email="pernillastrandberg87@gmail.com",
        day="2023-12-12",
        time="4 PM",
        guests="6",
    )

@pytest.fixture
def client():
    return Client()




def test_index_view(client):
    # Send GET request to "index" view using reverse function and Django test client
    response = client.get(reverse("index"))
    # Asserts that response status code is 200
    assert response.status_code == 200
    # Asserts correct template is used
    assert "index.html" in [template.name for template in response.templates]

def test_booking_list_view(client, booking):
    # Send GET request to "booking_list" view using reverse function and Django test client
    response = client.get(reverse("booking_list"))
    assert response.status_code == 200
    assert "booking_overview.html" in [template.name for template in response.templates]
    # Assuming response content contains string "Pernilla Strandberg"
    assert "Pernilla Strandberg" in response.content.decode('utf-8')

def test_booking_detail_view(client, booking):
    # Send GET request to "booking_detail" view for user-specific booking
    response = client.get(reverse("booking_detail", kwargs={"pk": booking.pk}))
    assert response.status_code == 200
    assert "booking.html" in [template.name for template in response.templates]
    # Assuming test user is connected to user-specific booking
    assert "Pernilla Strandberg" in response.content.decode('utf-8')

def test_booking_create_view(client):
    response = client.get(reverse("booking_create"))
    assert response.status_code == 200
    assert "booking_form.html" in [template.name for template in response.templates]

def test_booking_update_view(client, booking):
    response = client.get(reverse("booking_update", kwargs={"pk": booking.pk}))
    assert response.status_code == 200
    assert "booking_form_update.html" in [template.name for template in response.templates]

def test_booking_delete_view(client, booking):
    response = client.get(reverse("booking_delete", kwargs={"pk": booking.pk}))
    assert response.status_code == 200
    assert "booking_confirm_delete.html" in [template.name for template in response.templates]
    assert "Pernilla Strandberg" in response.content.decode('utf-8')





