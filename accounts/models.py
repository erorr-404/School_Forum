from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User, models.CASCADE, default=None)
    username = models.CharField(max_length=50)
    
