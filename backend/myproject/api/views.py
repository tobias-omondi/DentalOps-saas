# views for myproject
from django.shortcuts import render
# from django.http import HttpResponse , JsonResponse, Http404 , HttpResponseRedirect, HttpRequest, HttpResponseForbidden, HttpResponseNotAllowed
from rest_framework import viewsets
from .serializer import ClinicalDataSerializer, PatientDataSerializer, AppointmentDataSerializer, TreatmentDataSerializer , CommunicationDataSerializer, SubscriptionDataSerializer

from models.clinic import Clinic
from models.patient import Patient
from models.appointment import Appointment
from models.treatment import Treatment_Plan
from models.communication import Communication
from models.clinic_admin import Clinic_Admin
from models.subscription import Subscription

# --CLINIC VIEW SET
class ClinicViewSet(viewsets.ModelViewSet):
  queryset = Clinic.objects.all().order_by('name_of_clinic')
  serializer_class = ClinicalDataSerializer

#  --PATIENT VIEW SET--
class PatientViewSet (viewsets.ModelViewSet):
  queryset = Patient.objects.all().order_by('Full_name') #show all patients ordered by name
  serializer_class = PatientDataSerializer

# -- APPOINTMENT VIEW SET --
class AppointmentViewSet (viewsets.ModelViewSet):
  queryset = Appointment.objects.all()
  serializer_class = AppointmentDataSerializer

# ==TREATMENT VIEW SET==
class TreatmentViewSet (viewsets.ModelViewSet):
  queryset = Treatment_Plan.objects.all()
  serializer_class =TreatmentDataSerializer

# == COMMUNICATION VIEW SET==
class CommunicationViewSet (viewsets.ModelViewSet):
  queryset = Communication.objects.all()
  serializer_class = CommunicationDataSerializer

# == CLINIC ADMIN VIEW SET ==
class ClinicAdminViewSet (viewsets.ModelViewSet):
  queryset = Clinic_Admin.objects.all()
  serializer_class = ClinicalDataSerializer

# == subscription view set ==
class SubscriptionViewSet (viewsets.ModelViewSet):
  queryset = Subscription.objects.all()
  serializer_class = SubscriptionDataSerializer
  
# ==CREATE OTHER VIEWS IF NEEDED==