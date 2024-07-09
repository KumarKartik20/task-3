# appointments/forms.py

from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    appointment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    doctor = forms.CharField(max_length=100)

    class Meta:
        model = Appointment
        fields = ['appointment_date', 'appointment_time', 'doctor']
