from rest_framework import viewsets
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer
