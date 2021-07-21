from rest_framework import serializers
from powtoon.models import Powtoon
from user.models import User
from user.serializers import UserSerializer


class PowtoonSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)

    class Meta:
        model = Powtoon
        fields = ['id', 'name', 'content', 'owner']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['owner'] = UserSerializer(instance.owner).data
        return representation
