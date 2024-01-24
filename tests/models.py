from django.db import models

from accounts.models import CustomUser
from tests.consts import C_DIFFICULTY_CHOICES


class Exercise(models.Model):
    name = models.CharField(max_length=128, unique=False)
    time_left = models.DurationField()
    difficulty = models.CharField(max_length=64, choices=C_DIFFICULTY_CHOICES)

    @classmethod
    def get_time_left(cls, obj):
        return obj.time_left.total_seconds()


class ClassRoom(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False, blank=False)
    code = models.CharField(max_length=32, unique=True, null=False, blank=False)
    exercises = models.ManyToManyField(Exercise, null=True, blank=True)
    users = models.ManyToManyField(CustomUser, null=False, blank=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
