from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    PERMISSION_STATUSES = [
        ('USR', 'User'),
        ('MOD', 'Moderator'),
        ('ADM', 'Admin')
    ]
    password = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True, blank=False)
    about = models.TextField(max_length=256, blank=True)
    rank = models.SlugField(
        max_length=3,
        choices=PERMISSION_STATUSES,
        default='USR'
    )
    auth_code = models.CharField(max_length=9, blank=True)
