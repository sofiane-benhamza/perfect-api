from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=64)
    speciality = models.CharField(max_length=16)
    price = models.IntegerField()
    review_number = models.IntegerField()
    review_score = models.IntegerField()

class CompletedCourses(models.Model):
    start_date = models.DateField()
    finish_date = models.DateField()
    user_student = models.ForeignKey(UserStudent, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

class ReviewsCourse(models.Model):
    given_score = models.IntegerField()
    date = models.DateField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    
class Certificate(models.Model):
    completed_course = models.ForeignKey(CompletedCourses, on_delete=models.CASCADE)
    user_student = models.ForeignKey(UserStudent, on_delete=models.CASCADE)
    
class Quiz(models.Model):
    question = models.CharField(max_length=256)
    rep_A = models.CharField(max_length=256)
    rep_B = models.CharField(max_length=256)
    rep_C = models.CharField(max_length=256)
    time_to_answer = models.IntegerField()
    answer = models.CharField(max_length=256)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
