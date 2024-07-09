# appointments/models.py

from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    speciality = models.CharField(max_length=100)

    def __str__(self):
        return self.user.get_full_name()

class Appointment(models.Model):
    doctor = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"Appointment with {self.doctor.user.get_full_name()} on {self.start_time.strftime('%Y-%m-%d %H:%M')}"
