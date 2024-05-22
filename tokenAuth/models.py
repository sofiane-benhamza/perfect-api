from django.db import models
from users.models import Student

class tokenAuth(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    token = models.TextField()
    expiration_time = models.DateTimeField()
    active = models.BooleanField(False) 

    class Meta:
        db_table = "token_auth"
