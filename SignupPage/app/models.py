from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

    
class Person(AbstractBaseUser):
    first_name = models.CharField("First Name", max_length=30)
    last_name = models.CharField("Last Name", max_length=30)
    email = models.EmailField("Email", max_length=70, unique=True)
    password = models.CharField("Password", max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.first_name
