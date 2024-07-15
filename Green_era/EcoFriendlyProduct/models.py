from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):

    # Override the related_name for groups and permissions to avoid conflicts
    groups = models.ManyToManyField(Group, verbose_name='Groups', blank=True, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name='User Permissions', blank=True,
                                              related_name='custom_user_permissions')
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.username