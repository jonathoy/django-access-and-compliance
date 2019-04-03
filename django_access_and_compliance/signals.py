import requests
from django.db import models
from django.conf import settings
from django.shortcuts import redirect

def ensure_compliant(sender, request, user, **kwargs):
    payload = { 'uniqname': user.username }
    response = requests.get(settings.ACCESS_AND_COMPLIANCE_VALIDATION_URL, params=payload)
    response.raise_for_status()

    if _is_compliant(response):
        return True
    elif settings.ACCESS_AND_COMPLIANCE_FORM_URL:
        redirect(settings.ACCESS_AND_COMPLIANCE_FORM_URL)
    else:
        return False

def _is_compliant(response):
    return response.text in settings.ACCESS_AND_COMPLIANCE_TRUTHY_VALUES
