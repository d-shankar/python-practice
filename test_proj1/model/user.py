from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    dob = models.DateField()
