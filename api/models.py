from django.db import models


class Permission(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=65, unique=True)


class PermissionGroup(models.Model):
    permissions = models.ManyToManyField(Permission, related_name='permissions_set')


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255, unique=True)
    group = models.ForeignKey(PermissionGroup, related_name='group_user_set', on_delete=models.CASCADE)


class Powtoon(models.Model):
    name = models.CharField(max_length=200)
    content = models.JSONField()
    owner = models.ForeignKey(User, related_name='owner_powtoon_set', on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, related_name='shared_with_powtoon_set')

