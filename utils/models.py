from django.db import models

from accounts.models import CustomUser


class ModelBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey( CustomUser, on_delete=models.PROTECT)

    class Meta:
        abstract = True
