from django.db import models


class AccessAndCompliance(models.Model):
    class Meta:
        managed = False

        default_permissions = ()

        permissions = (
            ('confirmed_access_and_compliance',
             'Attested to access and compliance policy'),
        )
