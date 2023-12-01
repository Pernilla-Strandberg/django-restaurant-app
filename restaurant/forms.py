from django import forms
from .models import BookingModel

class BookingModelForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = '__all__'
        widgets = {
            'day': forms.DateInput(attrs={'type': 'date'}),
        }
        exclude = ['user']