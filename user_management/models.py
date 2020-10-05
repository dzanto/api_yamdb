from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER = 'USR'
    MODER = 'MOD'
    ADMIN = 'ADM'
    PERMISSION_STATUSES = [
        (USER, 'User'),
        (MODER, 'Moderator'),
        (ADMIN, 'Admin')
    ]
    email = models.EmailField(unique=True, blank=False)
    about = models.TextField(max_length=256, blank=True)
    rank = models.SlugField(
        max_length=3,
        choices=PERMISSION_STATUSES,
        default=USER
    )
    auth_code = models.CharField(max_length=9, blank=True)
