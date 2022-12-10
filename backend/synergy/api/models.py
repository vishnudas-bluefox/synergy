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

class usertable(models.Model):
    consumerno = models.IntegerField(default=0,unique=True)
    name = models.CharField(max_length=100)
    bpoint = models.IntegerField(default=0)
    tcredit = models.IntegerField(default=0)
    ucredit = models.IntegerField(default=0)
    monthlycap = models.IntegerField(default=0)
