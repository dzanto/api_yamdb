from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    PERMISSION_STATUSES = [
        ('user', 'User'),
        ('moderator', 'Moderator'),
        ('admin', 'Admin')
    ]
    password = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True, blank=False)
    bio = models.TextField(max_length=256, blank=True)
    role = models.SlugField(
        max_length=9,
        choices=PERMISSION_STATUSES,
        default='user'
    )
    auth_code = models.CharField(max_length=9, blank=True)
