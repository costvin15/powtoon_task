from rest_framework import serializers
from share.models import PermissionGroup


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PermissionGroup
        fields = ['name', 'permissions']
