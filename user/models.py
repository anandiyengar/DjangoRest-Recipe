from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(AbstractUser):
    GENDER_CHOICE = [
        ('Male','Male'),
        ('Male','Male'),
        ('Other','Other'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    weight = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=255, default="")
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email