from django.db import models
from django.contrib.auth.models import User
from .patient import Patient
from .clinic import Clinic
# Treatment_plan modles representation of dental treatment plans

class Treatment_Plan(models.Model):
  clinic = models.ForeignKey(Clinic, on_delete = models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  diagnosis = models.TextField()
  treatment_details = models.TextField()
  start_date = models.DateField()
  end_date = models.DateField()
  status = models.CharField(max_length=50)
  created_at = models.DateTimeField( auto_now_add=True)
  upadated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"Treatment plan for {self.patient.Full_name} at {self.clinic.name}"