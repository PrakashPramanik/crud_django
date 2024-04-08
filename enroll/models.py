from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    password = models.CharField(max_length=30)
