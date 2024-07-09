# appointments/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Doctor, Appointment
from .forms import AppointmentForm
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle
from datetime import datetime, timedelta
from django.contrib import messages


SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_google_calendar_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds)
    return service


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'appointments/doctor_list.html', {'doctors': doctors})
# appointments/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Doctor, Appointment
from .forms import AppointmentForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Doctor, Appointment
from .forms import AppointmentForm
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm
from datetime import datetime, timedelta

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment_date = form.cleaned_data['appointment_date']
            appointment_time = form.cleaned_data['appointment_time']
            doctor = form.cleaned_data['doctor']

            start_datetime = datetime.combine(appointment_date, appointment_time)
            end_datetime = start_datetime + timedelta(minutes=45)

            appointment = Appointment(
                doctor=doctor,
                start_time=start_datetime,
                end_time=end_datetime,
            )
            appointment.save()
            messages.success(request, 'Appointment booked successfully.')
            return redirect('doctor_list')
    else:
        form = AppointmentForm()

    return render(request, 'appointments/book_appointments.html', {'form': form})
def appointment_details(request):
    appointment = get_object_or_404(Appointment)
    return render(request, 'appointments/appointment_details.html', {'appointment': appointment})
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

class SignUpView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('login'))
        return render(request, 'registration/signup.html', {'form': form})