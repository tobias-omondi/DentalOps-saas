from django.contrib import admin
from .clinic import Clinic
from .patient import Patient
from .appointment import Appointment
from .communication import Communication
from .treatment import Treatment_Plan
from .subscription import Subscription
from .clinic_admin import Clinic_Admin

# Register all your models
admin.site.register(Clinic)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Communication)
admin.site.register(Treatment_Plan)
admin.site.register(Subscription)
admin.site.register(Clinic_Admin)