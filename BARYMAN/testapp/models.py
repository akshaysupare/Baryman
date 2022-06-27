import email
from operator import mod
from django.db import models

from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    product = models.CharField(max_length=20)
    massage = models.TextField()
    date = models.DateTimeField()