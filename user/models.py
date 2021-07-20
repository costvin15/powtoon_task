from django.db import models
from share.models import Group


class User(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=65, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(Group, through='UserGroup')

    class Meta:
        ordering = ['created']


class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
