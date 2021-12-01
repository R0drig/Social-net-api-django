from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class UserFollow(models.Model):
    following = models.ManyToManyField(User, related_name='following')
    follower = models.ManyToManyField(User, related_name='follower')
