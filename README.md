=====
Access and Compliance
=====

Access and compliance is a simple Django app to check and verify a
user's acceptance of University of Michigan's Access and Compliance
policy.

Quick start
-----------

1. Add "accessandcompliance" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'accessandcompliance',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('accessandcompliance/', include('accessandcompliance.urls')),

3. Run `python manage.py migrate` to create the access and compliance models.
