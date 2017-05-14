from __future__ import unicode_literals

from django.db import models

# Create your models here.
# http://stackoverflow.com/a/43209322/185820
# from django.contrib.auth.models import AbstractUser
#class User(AbstractUser):
#    USERNAME_FIELD = 'email'
#    email = models.EmailField(_('email address'), unique=True) # changes email to unique and blank to false
#    REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
