from django.db import models
from django.contrib.auth.models import User
from .clinic import Clinic

# Subscription models representation of clinic subscription
class Subscription(models.Model):
  Clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
  payment_method = models.CharField(max_length=50)
  plan_type = models.CharField(max_length=50)
  start_date = models.DateField()
  end_date = models.DateField()
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
  updated_at = models.DateTimeField(auto_created=True,
                                    auto_now=True)
  
  def __str__(self):
    return super().__str__()