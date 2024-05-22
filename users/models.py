from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=128)
    is_male = models.BooleanField()
    level = models.CharField(max_length=128)