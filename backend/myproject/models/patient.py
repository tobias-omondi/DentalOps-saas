from django.db import models
from django.contrib.auth.models import User

# Patient models representation of a dental patient
class Patient(models.Model):
  Full_name = models.CharField(max_length=255)
  date_of_birth = models.DateField()
  email = models.EmailField()
  phone_number = models.CharField(max_length=20)
  address = models.CharField(max_length=255, blank=True, null=True)
  clinic = models.ForeignKey('Clinic', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_created=True,
                                    auto_now_add=True)
  updated_at = models.DateTimeField(auto_created =True, auto_now=True)

  def __str__(self):
    return self.Full_name