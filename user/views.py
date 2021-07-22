from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from user.serializers import UserSerializer
from powtoon.models import Powtoon
from powtoon.serializers import PowtoonSerializer
from share.models import Group


class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
        method='GET',
        operation_description='This route lists all the powtoons shared with the logged in user',
        responses={
            200: UserSerializer,
            400: 'Bad request'
        }
    )
    @action(detail=True)
    def shared_with_me(self, request, *args, **kwargs):
        user = self.get_object()
        powtoons = Powtoon.objects.filter(shared_with__pk=user.pk)
        serializer = PowtoonSerializer(powtoons, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        method='POST',
        operation_description='This route allows you to add a user to a group',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'group': openapi.Schema(type=openapi.TYPE_INTEGER, description='Group ID')
            }
        ),
        responses={
            200: UserSerializer,
            400: 'Bad request'
        }
    )
    @action(detail=True, methods=['post'])
    def add_to_group(self, request, *args, **kwargs):
        user = self.get_object()
        group = Group.objects.get(pk=request.data.get('group'))
        user.groups.add(group)
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)
