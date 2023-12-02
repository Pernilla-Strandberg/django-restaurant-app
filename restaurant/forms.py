from django import forms

from .models import BookingModel


class BookingModelForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = "__all__"
        widgets = {
            "day": forms.DateInput(attrs={"type": "date"}),
            "first_name": forms.TextInput(attrs={"placeholder": "First Name",}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name",}),
            "email": forms.TextInput(attrs={"placeholder": "example@email.com",})
        }
        exclude = ["user"]