from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from user.models import User
from share.serializers import GroupSerializer


class UserSerializer(WritableNestedModelSerializer, serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'groups']
