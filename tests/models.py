from django.db import models

from accounts.models import CustomUser
from tests.consts import C_DIFFICULTY_CHOICES

from utils.models import ModelBase


class Exercise(ModelBase):
    name = models.CharField(max_length=128, unique=False)
    time = models.DurationField()
    difficulty = models.CharField(max_length=64, choices=C_DIFFICULTY_CHOICES)
    created_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='created_exercise')

    @classmethod
    def get_time_left(cls, obj):
        return obj.time.total_seconds()


class ClassRoom(ModelBase):
    name = models.CharField(max_length=128, unique=True)
    code = models.CharField(max_length=16, unique=True)
    exercises = models.ManyToManyField(Exercise, blank=True)
    members = models.ManyToManyField(CustomUser, blank=False, related_name='members_classrooms')
    created_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='created_classrooms')

    def __str__(self):
        return self.name
