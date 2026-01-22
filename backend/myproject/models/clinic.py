from django.db import models
from django.contrib.auth.models import User

# clinic models representation of a dental clinic
class Clinic(models.Model):
  name =models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  phone_number = models.CharField(max_length=20)
  email = models.EmailField()
  password = models.CharField(max_length=128)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
  updated_at = models.DateTimeField(auto_created =True, auto_now=True)

  def __str__(self):
    return self.name