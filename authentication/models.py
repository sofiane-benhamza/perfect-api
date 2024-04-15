from django.db import models

class UserStudent(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=128)
    is_male = models.BooleanField()
    level = models.CharField(max_length=64)

class UserProf(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    etablissement = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(max_length=64, unique=True)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=128)
    speciality = models.CharField(max_length=32)
    is_male = models.BooleanField()
    
class Diploma(models.Model):
    user_prof = models.ForeignKey(UserProf, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, unique=True)
    start_date = models.CharField(max_length=7)
    end_date = models.CharField(max_length=7)    #XXXX-XX
    
class ReviewsProf(models.Model):
    given_score = models.IntegerField()
    date = models.DateField()
    scorer = models.ForeignKey(UserStudent, on_delete=models.CASCADE)
    user_prof = models.ForeignKey(UserProf, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('scorer', 'user_prof'),)        
    
class Experience(models.Model):
    user_prof = models.ForeignKey(UserProf, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, unique=True)
    start_date = models.CharField(max_length=12)  ##string  2012-06-07  XXXX-XX-XX
    end_date = models.CharField(max_length=12)
    

