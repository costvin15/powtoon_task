from rest_framework import viewsets
from powtoon.models import Powtoon
from powtoon.serializers import PowtoonSerializer


class PowtoonViewSet(viewsets.ModelViewSet):
    queryset = Powtoon.objects.all()
    serializer_class = PowtoonSerializer
