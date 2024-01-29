from django.contrib.auth.models import AbstractUser
from django.db import models

from .consts import USER_TYPE_CHOICES


class UserInventory(models.Model):
    pass


class CustomUser(AbstractUser):
    type = models.CharField(max_length=20, default="Student", choices=USER_TYPE_CHOICES)
    inventory = models.ForeignKey(UserInventory, null=True, blank=True, on_delete=models.CASCADE)
