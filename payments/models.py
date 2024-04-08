from django.db import models

class Payments(models.Model):
    date = models.DateField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    user_student = models.ForeignKey(UserStudent, on_delete=models.CASCADE)
