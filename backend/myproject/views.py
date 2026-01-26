# views for myproject
from django.shortcuts import render
# from django.http import HttpResponse , JsonResponse, Http404 , HttpResponseRedirect, HttpRequest, HttpResponseForbidden, HttpResponseNotAllowed
from rest_framework import viewsets
from .serializer import ClinicalDataSerializer, PatientDataSerializer, AppointmentDataSerializer, TreatmentDataSerializer , CommunicationDataSerializer, SubscriptionDataSerializer

from .models import Clinic, Patient, Appointment, Treatment_Plan, Communication, Clinic_Admin, Subscription

# --CLINIC VIEW SET
class ClinicViewSet(viewsets.ModelViewSet):
  queryset = Clinic.objects.filter(active = True).order_by('name') # show onlt active clinics
  serializer_class = ClinicalDataSerializer

#  --PATIENT VIEW SET--
class PatientViewSet (viewsets.ModelViewSer):
  queryset = Patient.objects.all().order_by('name') #show all patients ordered by name
  serializer_class = PatientDataSerializer

# -- APPOINTMENT VIEW SET --
class AppointmentViewSet (viewsets.ModelViewSet):
  queryset = Appointment.objects.all().order_by('appointment_date')
  serializer_class = AppointmentDataSerializer

# ==TREATMENT VIEW SET==
class TreatmentViewSet (viewsets.ModelViewSet):
  queryset = Treatment_Plan.objects.all().order_by('treatment_name')
  serializer_class =TreatmentDataSerializer

# == COMMUNICATION VIEW SET==
class CommunicationViewSet (viewsets.ModelViewSet):
  queryset = Communication.objects.all().order_by('sent_at')
  serializer_class = CommunicationDataSerializer

# == CLINIC ADMIN VIEW SET ==
class ClinicAdminViewSet (viewsets.ModelViewSet):
  queryset = Clinic_Admin.objects,all()
  serializer_class = ClinicalDataSerializer

# == subscription view set ==
class SubscriptionViewSet (viewsets.ModelViewSet):
  queryset = SubscriptionDataSerializer.abjects.all()
  serializer_class = SubscriptionDataSerializer
  
# ==CREATE OTHER VIEWS IF NEEDED==