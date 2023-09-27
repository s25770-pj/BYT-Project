from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.utils.translation import gettext as _


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_blocked = models.BooleanField(default=False)
    ROLE_CHOICES = (
        ('user', 'Użytkownik'),
        ('admin', 'Administrator'),
        ('moderator', 'Moderator'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )
