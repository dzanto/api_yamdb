from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    PERMISSION_STATUSES = [
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin')
    ]
    password = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True, blank=False)
    bio = models.TextField(max_length=256, blank=True)
    username = models.CharField(max_length=50, unique=True)
    role = models.CharField(
        max_length=10,
        choices=PERMISSION_STATUSES,
        default='user'
    )
    auth_code = models.CharField(max_length=9, blank=True)
