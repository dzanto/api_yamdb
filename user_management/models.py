from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    class Role(models.TextChoices):
        USER = 'user', _('User')
        MODERATOR = 'moderator', _('Moderator')
        ADMIN = 'admin', _('Admin')

    password = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True, blank=False)
    bio = models.TextField(max_length=256, blank=True)
    username = models.CharField(max_length=50, unique=True)
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.USER
    )

    @property
    def is_admin(self):
        if self.role == self.Role.ADMIN or self.is_superuser:
            return True
        return False

    @property
    def is_moderator(self):
        if self.role == self.Role.MODERATOR:
            return True
        return False
