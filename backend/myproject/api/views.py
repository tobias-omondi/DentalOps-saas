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

# import authentication and permissions
from rest_framework.permissions import IsAuthenticated


# --CLINIC VIEW SET
class ClinicViewSet(viewsets.ModelViewSet):
  queryset = Clinic.objects.all().order_by('name_of_clinic')
  serializer_class = ClinicalDataSerializer

  # ++ add authentication and permission classes
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    user = self.request.user
    return self.queryset.filter(owner=user).order_by('name_of_clinic')
  



#  == PATIENT VIEW SET ==
class PatientViewSet (viewsets.ModelViewSet):
  queryset = Patient.objects.all().order_by('full_name') #show all patients ordered by name
  serializer_class = PatientDataSerializer

  # ++ add authentication and permission classes
  permission_classes = [IsAuthenticated]

  # isolate patients by clinic
  def get_queryset(self):
    clinic_id = self.request.query_params.get('clinic_id', None)
    user = self.request.user
    
    # Allow superusers to see all patients (for development/testing)
    if user.is_superuser:
      if clinic_id is not None:
        return self.queryset.filter(clinic_id=clinic_id)
      return self.queryset
    
    # Get clinics the user is authorized for
    user_clinics = Clinic_Admin.objects.filter(admin_user=user).values_list('clinic_id', flat=True)
    
    if clinic_id is not None:
      # Verify user has access to this clinic
      if int(clinic_id) not in user_clinics:
        return self.queryset.none()  # Return empty queryset
      return self.queryset.filter(clinic_id=clinic_id)
    
    # If no clinic_id specified, show patients only from clinics user manages
    return self.queryset.filter(clinic_id__in=user_clinics)



# -- APPOINTMENT VIEW SET --
class AppointmentViewSet (viewsets.ModelViewSet):
  queryset = Appointment.objects.all()
  serializer_class = AppointmentDataSerializer

  # ++ add authentication and permission classes
  permission_classes = [IsAuthenticated]



# ==TREATMENT VIEW SET==
class TreatmentViewSet (viewsets.ModelViewSet):
  queryset = Treatment_Plan.objects.all()
  serializer_class =TreatmentDataSerializer

  # ++ add authentication and permission classes
  permission_classes = [IsAuthenticated]

# == COMMUNICATION VIEW SET==
class CommunicationViewSet (viewsets.ModelViewSet):
  queryset = Communication.objects.all()
  serializer_class = CommunicationDataSerializer

  # ++ add authentication and permission classes
  permission_classes = [IsAuthenticated]

# == CLINIC ADMIN VIEW SET ==
class ClinicAdminViewSet (viewsets.ModelViewSet):
  queryset = Clinic_Admin.objects.all()
  serializer_class = ClinicalDataSerializer

  # ++ add authentication and permission classes
  permission_classes = [IsAuthenticated]

# == subscription view set ==
class SubscriptionViewSet (viewsets.ModelViewSet):
  queryset = Subscription.objects.all()
  serializer_class = SubscriptionDataSerializer

  # ++ add authentication and permission classes
  permission_classes = [IsAuthenticated]
  
# ==CREATE OTHER VIEWS IF NEEDED==