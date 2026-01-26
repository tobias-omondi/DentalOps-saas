from django.db import models
from django.contrib.auth.models import User
from .clinic import Clinic
# administarative models representation of clinic administrators

class Clinic_Admin(models.Model):
  clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
  admin_user = models.ForeignKey(User, on_delete=models.CASCADE)
  role = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.admin_user.username} - {self.clinic.name} as {self.role}"