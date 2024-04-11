from django.db import models
from authentication.models import UserStudent
from courses.models import Courses
class Payments(models.Model):
    date = models.DateField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    user_student = models.ForeignKey(UserStudent, on_delete=models.CASCADE)
