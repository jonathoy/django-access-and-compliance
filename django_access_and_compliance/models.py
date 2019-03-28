from django.db import models
from django.contrib.auth.signals import user_logged_in

def check_access_and_compliance(sender, request, user):
    print('>>>>>>>>>> Logged in!!!!')

user_logged_in.connect(check_access_and_compliance)
