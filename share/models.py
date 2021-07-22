from django.db import models


class Permission(models.Model):
    code = models.CharField(max_length=65, unique=True)
    name = models.CharField(max_length=200)


class Group(models.Model):
    name = models.CharField(max_length=128)
    permissions = models.ManyToManyField(Permission, through='PermissionGroup')


class PermissionGroup(models.Model):
    """
    Represents the many to many relationship of a group with a permission.
    """
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
