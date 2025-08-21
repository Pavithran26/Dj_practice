from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone =models.IntegerField(null=True)
    dob=models.DateField(null=True)
