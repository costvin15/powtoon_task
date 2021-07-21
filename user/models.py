from django.db import models
from django.contrib.auth.models import AbstractUser
from share.models import Group

from user.managers import UserManager


class User(AbstractUser):
    name = models.CharField(max_length=100, blank=True, default='')
    username = models.CharField(max_length=130, blank=False, default='')
    email = models.EmailField(max_length=255, unique=True, default='')
    password = models.CharField(max_length=130, blank=False, default='')
    created = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(Group, through='UserGroup')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [email, password]
    objects = UserManager()


class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
