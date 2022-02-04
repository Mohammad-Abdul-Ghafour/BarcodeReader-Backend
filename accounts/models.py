import imp
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    role = models.CharField(max_length=50 , choices=(('Manager','Manager'),('User','User')), default='User')

    def __str__(self):
        return self.username

