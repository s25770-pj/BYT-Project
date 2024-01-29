from django.contrib.auth.models import AbstractUser
from django.db import models

USER_TYPE_CHOICES = [
    ('nauczyciel', 'Teacher'),
    ('uczeń', 'Student')
]


class UserEquipment(models.Model):
    pass


class CustomUser(AbstractUser):
    type = models.CharField(max_length=20, default="Student", choices=USER_TYPE_CHOICES)
    equipment = models.ForeignKey(UserEquipment, null=True, blank=True, on_delete=models.CASCADE)
