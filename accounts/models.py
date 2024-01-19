from django.contrib.auth.models import AbstractUser
from django.db import models


class UserEquipment(models.Model):
    pass


class CustomUser(AbstractUser):
    equipment = models.ForeignKey(UserEquipment, null=True, blank=True, on_delete=models.CASCADE)
