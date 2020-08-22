from django.db import models

# Create your models here.
class MyUser(models.Model):
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120)