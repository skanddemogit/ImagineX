from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, null=True, blank=True)

    REQUIRED_FIELDS = ['age', 'gender', 'email']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
