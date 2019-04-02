from django.apps import AppConfig
from .models import ensure_compliant
from django.contrib.auth.signals import user_logged_in

class AccessAndComplianceConfig(AppConfig):
    name = 'access_and_compliance'
    verbose = 'Access and Compliance'

    def ready(self):
        user_logged_in.connect(ensure_compliant)
