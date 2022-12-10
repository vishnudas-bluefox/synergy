from django.db import models
from django.contrib.auth.models import AbstractUser



class user(AbstractUser):
    name = models.CharField(max_length=50)
    consumerno = models.CharField(max_length=50,unique=True)
    email = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=100)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
