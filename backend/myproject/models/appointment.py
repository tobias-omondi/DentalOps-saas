from django.db import models
from django.contrib.auth.models import User
from .patient import Patient
from .clinic import Clinic

# Appointment models representation of dental appointments
class Appointment (models.Model):
  Clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  Appointment_date = models.DateTimeField()
  Appointment_time = models.TimeField()
  reason_for_visit = models.TextField()
  location = models.CharField()
  created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
  updated_at = models.DateTimeField(auto_created=True, auto_now=True)

  def __str__(self):
    return f"Appointment for {self.patient.Full_name} at {self.Clinic.name} on {self.Appointment_date} at {self.Appointment_time}"