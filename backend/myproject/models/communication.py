from django.db import models

# communication models representation of messages between clinic and patients
class Communication(models.Model):
  patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
  clinic = models.ForeignKey("Clinic", on_delete= models.CASCADE)
  title = models.CharField(max_length=300)
  message =models.TextField()
  sent_at = models.DateTimeField(auto_created=True,
                                 auto_now_add=True)
  status = models.CharField(max_length=50)
  read = models.BooleanField(default=False)

  def __str__(self):
    return f"message to {self.patient.Full_name} from {self.clinic.name}"