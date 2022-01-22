from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager
# Create your models here.





class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
