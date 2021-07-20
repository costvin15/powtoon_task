from django.db import models
from user.models import User


class Powtoon(models.Model):
    name = models.CharField(max_length=200)
    content = models.JSONField()
    owner = models.ForeignKey(User, related_name='powtoons', on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, through='PowtoonShared')


class PowtoonShared(models.Model):
    powtoon = models.ForeignKey(Powtoon, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
