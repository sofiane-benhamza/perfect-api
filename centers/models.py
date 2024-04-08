from django.db import models

class Center(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    email = models.EmailField(max_length=64)
    phone = models.CharField(max_length=16)
    capacity_of_students = models.IntegerField()

class AvailabilityOfCenter(models.Model):
    salle_name = models.CharField(max_length=32)
    course_name = models.CharField(max_length=32)
    taken_by_students = models.IntegerField()
    capacity_of_students = models.IntegerField()
    start_date = models.DateField()
    number_of_hours = models.IntegerField()
