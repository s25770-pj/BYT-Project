from django.contrib.auth.models import AbstractUser
from django.db import models

TypeChoices = [
    ('uczeń', 'Student'),
    ('nauczyciel', 'Teacher')
]


class UserEquipment(models.Model):
    pass


class CustomUser(AbstractUser):
    type = models.CharField(max_length=20, verbose_name='Typ', choices=TypeChoices, default=TypeChoices[0])
    equipment = models.ForeignKey(UserEquipment, null=True, blank=True, on_delete=models.CASCADE)
