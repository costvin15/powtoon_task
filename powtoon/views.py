from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from powtoon import permissions
from powtoon.models import Powtoon
from powtoon.serializers import PowtoonSerializer


class PowtoonViewSet(viewsets.ModelViewSet):
    queryset = Powtoon.objects.all()
    serializer_class = PowtoonSerializer
    permission_classes = [IsAuthenticated, permissions.IsOwnerOrAdmin]
