# serialize the models to json (rules and validations)
from rest_framework import serializers
from .models import Clinic , Patient , Appointment, Treatment_Plan,  Communication, Clinic_Admin, Subscription


# --CLINIC SERIALIZER--
class ClinicalDataSerializer(serializers.ModelSerializer):
  class Meta:
    model = Clinic
    fields = '__all__'

#  --PATIENT SERIALIZER--
class PatientDataSerializer (serializers.ModelSerializer):
  class Meta:
    model = Patient
    fields = '__all__'

# -- APPOINTMENT SERIALIZER--

class AppointmentDataSerializer (serializers.ModelSerializer):
  class Meta:
    model = Appointment
    fields = '__all__'

# --TREATMENT SERIALIZER--
class TreatmentDataSerializer (serializers.ModelSerializer):
  class Meta:
    model = Treatment_Plan
    fields = '__all__'

# --COMMUNICATION SERIALIZER--
class CommunicationDataSerializer (serializers.ModelSerializer):
  class Meta:
    model = Communication
    fields = '__all__'

# --CLINIC ADMIN SERIALIZER-

class clinicAdminDataSerializer (serializers.ModelSerializer):
  class Meta:
    model = Clinic_Admin
    fields = '__all__'

# --SUBSCRIPTION SERIALIZER --
class SubscriptionDataSerializer (serializers.ModelSerializer):
  class Meta:
    model = Subscription
    fields = '__all__'

 