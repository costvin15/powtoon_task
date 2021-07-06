from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=64)


class Powtonn(models.Model):
    name = models.CharField(max_length=200)
    content = models.JSONField()
    owner = models.ForeignKey(User, related_name='owner_powtoon_set', on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, related_name='shared_with_powtoon_set')
