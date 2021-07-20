from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=65, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


class Permission(models.Model):
    code = models.CharField(max_length=65, unique=True)
    name = models.CharField(max_length=200)


class Group(models.Model):
    name = models.CharField(max_length=128)
    users = models.ManyToManyField(User, through='UserGroup')
    permissions = models.ManyToManyField(Permission, through='PermissionGroup')


class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class PermissionGroup(models.Model):
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
