from django.db import models

def ensure_compliant(sender, request, user):
    print('>>>>>>>>>> Logged in!!!!')
