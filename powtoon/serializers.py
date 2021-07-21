from rest_framework import serializers
from powtoon.models import Powtoon
from user.models import User


class PowtoonSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)

    class Meta:
        model = Powtoon
        fields = ['id', 'name', 'content', 'owner']
