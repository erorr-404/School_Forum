from email.policy import default
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    image = models.ImageField(upload_to='media/profile_pics/', default='default.jpg')
    biography = models.TextField(default='')

    def __str__(self):
        return f'{self.user.username} Profile'