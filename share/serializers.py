from rest_framework import serializers
from share.models import Group, Permission


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'code', 'name']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']
