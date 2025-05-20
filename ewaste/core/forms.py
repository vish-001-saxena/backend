from django import forms
from .models import Registration, PickupRequest

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'phone',]

class PickupForm(forms.ModelForm):
    class Meta:
        model = PickupRequest
        fields = ['name', 'email', 'address', 'device_type', 'scheduled_date']

