from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField("First Name", max_length=30)
    last_name = models.CharField("Last Name", max_length=30)
    email = models.EmailField("Email", max_length=70)
    password = models.CharField("Password", max_length=30)

    def __str__(self):
        return self.first_name
