from rest_framework import serializers
from powtoon.models import Powtoon


class PowtoonSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Powtoon
        fields = ['id', 'name', 'content', 'owner', 'owner']
