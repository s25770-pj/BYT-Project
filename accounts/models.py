from django.contrib.auth.models import AbstractUser
from django.db import models

userChoices = [
    ('nauczyciel', 'Teacher'),
    ('uczeń', 'Student')
]


class UserEquipment(models.Model):
    pass


class CustomUser(AbstractUser):
    type = models.CharField(max_length=10, default="user", choices=userChoices)
    equipment = models.ForeignKey(UserEquipment, null=True, blank=True, on_delete=models.CASCADE)
