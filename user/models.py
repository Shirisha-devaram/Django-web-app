from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    username=models.CharField(max_length=255,unique=True)
    email=models.CharField(max_length=255,unique=True)
    password=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','password']