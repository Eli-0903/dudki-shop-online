import email
from django.db import models

# Create your models here.

class Profile(models.Model):
    full_name = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.IntegerField()
    
    def __str__(self):
        return self.name
    