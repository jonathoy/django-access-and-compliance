import requests
from django.conf import settings
from django.contrib.auth.models import Permission

def ensure_compliant(sender, request, user, **kwargs):
    payload = {'uniqname': user.username}
    response = requests.get(settings.ACCESS_AND_COMPLIANCE_VALIDATION_URL, params=payload)
    response.raise_for_status()

    if _is_compliant(response):
        permission = Permission.objects.get(codename='confirmed_access_and_compliance')
        user.user_permissions.add(permission)
    else:
        print(f'{user} has not attested to data compliance policy!')

def _is_compliant(response):
    return response.text in settings.ACCESS_AND_COMPLIANCE_TRUTHY_VALUES
