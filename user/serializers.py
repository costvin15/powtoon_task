from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from user.models import User
from share.serializers import GroupSerializer
from powtoon.serializers import PowtoonSerializer


class UserSerializer(WritableNestedModelSerializer, serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)
    powtoons = PowtoonSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'groups', 'powtoons']
