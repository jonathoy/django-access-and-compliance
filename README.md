# Access and Compliance

Access and compliance is a simple Django app to check and verify a
user's acceptance of University of Michigan's Access and Compliance
policy.

## Quick start

1. Add "django_access_and_compliance" to your INSTALLED_APPS setting like this::

   INSTALLED_APPS = [
   'django_access_and_compliance',
   ...
   ]

2. Run `python manage.py migrate` to create the access and compliance models.

3. Configure the following settings in your application:

```python
# the URL for the desired access and compliance webservice
ACCESS_AND_COMPLIANCE_VALIDATION_URL

# truthy values returned by validation endpoint; e.g. true, yes, etc.
ACCESS_AND_COMPLIANCE_TRUTHY_VALUES
```

## Behavior

This application hooks into an existing Django application and listens for the login signal. Once a user logs in, it makes a request to the `ACCESS_AND_COMPLIANCE_VALIDATION_URL` and checks if the response body matches one of the truthy values specified in `ACCESS_AND_COMPLIANCE_TRUTHY_VALUES`.

If the user has attested to the data access and compliance policy, an auth permission will be added for the user.

It will resemble the following structure:

```python
from django.contrib.auth.models import Permission

from .models import AccessAndCompliance

content_type = ContentType.objects.get_for_model(AccessAndCompliance)
Permission.objects.get(
    codename='confirmed_access_and_compliance',
    content_type=content_type,
    name='Attested to access and compliance policy'
)
```

From your Django application, you can then validate for the permission by utilizing the [built-in permissions methods](https://docs.djangoproject.com/en/2.2/topics/auth/default/#permissions-and-authorization).

e.g. with a decorator

```python
@permission_required('django_access_and_compliance.confirmed_access_and_compliance', raise_exception=True)
def protected_view(request):
    # view stuff
```
