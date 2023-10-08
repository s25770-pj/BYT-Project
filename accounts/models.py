from django.utils.translation import gettext as _
from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, PermissionsMixin, Group


class Parent(AbstractUser, PermissionsMixin):
    login = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_blocked = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('Grupy'),
        blank=True,
        related_name='parent_set',
        related_query_name='parent'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('Uprawnienia użytkownika'),
        blank=True,
        related_name='parent_user_permissions',
        related_query_name='user'
    )
    role = models.CharField(max_length=20, default='Rodzic')

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'Rodzic'
        verbose_name_plural = 'Rodzice'


class Child(models.Model):
    role = models.CharField(max_length=10, default='Dziecko')
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, blank=True, null=True, unique=True)
    password = models.CharField(max_length=50, blank=False, null=False)
    profile_picture = models.ImageField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = 'Dziecko'
        verbose_name_plural = 'Dzieci'
