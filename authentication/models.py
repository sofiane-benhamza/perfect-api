from django.db import models

class UserStudent(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=128)
    isMale = models.BooleanField()
    level = models.CharField(max_length=64)

class UserProf(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    etablissement = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(max_length=64)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=128)
    speciality = models.CharField(max_length=32)
    review_number = models.IntegerField()
    review_score = models.IntegerField()
    isMale = models.BooleanField()
    
class Diploma(models.Model):
    name = models.CharField(max_length=64)
    date = models.CharField(max_length=16)
    
class ReviewsProf(models.Model):
    given_score = models.IntegerField()
    date = models.DateField()
    user_prof = models.ForeignKey(UserProf, on_delete=models.CASCADE)
    
class Experience(models.Model):
    name = models.CharField(max_length=64)
    date = models.CharField(max_length=16)
    

