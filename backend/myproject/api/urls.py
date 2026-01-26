# urls for dental ops app
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClinicViewSet, PatientViewSet , AppointmentViewSet, TreatmentViewSet, CommunicationViewSet, SubscriptionViewSet, ClinicAdminViewSet

router = DefaultRouter()

# register viewsets with the router
router.register(r'clinics', ClinicViewSet, basename='clinic')
router.register(r'patients', PatientViewSet,)
router.register(r'appointments', AppointmentViewSet)
router.register(r'treatments', TreatmentViewSet)
router.register(r'communications', CommunicationViewSet)
router.register(r'clinic-admins', ClinicAdminViewSet, basename='clinic-admin')
router.register(r'subscriptions', SubscriptionViewSet)


urlpatterns = [
  path('', include(router.urls)),
]