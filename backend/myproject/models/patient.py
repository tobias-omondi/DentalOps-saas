from django.db import models
from django.contrib.auth.models import User
from .clinic import Clinic

# Patient models representation of a dental patient
class Patient(models.Model):
  full_name = models.CharField(max_length=255)
  date_of_birth = models.DateField()
  email = models.EmailField()
  phone_number = models.CharField(max_length=20)
  national_id = models.CharField(max_length=50, blank=True, null=True)
  address = models.CharField(max_length=255, blank=True, null=True)
  clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='patients')
  next_of_kin_name = models.CharField(max_length=255, blank=True, null=True)
  # medical history fields
  medical_history = models.TextField( default='', help_text="Patient's medical history and conditions")
  allergies = models.TextField(True, default='', help_text="Known allergies (medications, materials,")
  medications = models.TextField(blank=True, default='', help_text="current medications the patient is taking")

  profile_completed = models.BooleanField(default=False)
  medical_info_verified = models.BooleanField(default=False)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.Full_name