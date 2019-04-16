import requests
import logging
from django.conf import settings
from django.contrib.auth.models import Permission

logger = logging.getLogger(__name__)

def ensure_compliant(sender, request, user, **kwargs):
    payload = {'uniqname': user.username}
    response = requests.get(settings.ACCESS_AND_COMPLIANCE_VALIDATION_URL, params=payload)
    response.raise_for_status()
    permission = Permission.objects.get(codename='confirmed_access_and_compliance')

    if _is_compliant(response):
        user.user_permissions.add(permission)
        logger.debug(f'{user} has attested to the data access and compliance policy')
    else:
        user.user_permissions.remove(permission)
        logger.debug(f'{user} has not attested to data compliance policy')

def _is_compliant(response):
    return response.text in settings.ACCESS_AND_COMPLIANCE_TRUTHY_VALUES
