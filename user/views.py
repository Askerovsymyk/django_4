
from django.shortcuts import render
from rest_framework.decorators import api_view
from user.serializers import UserCreateSerializer, UserAuthenticationSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
# Create your views here.


@api_view(['POST'])
def authenticate_api_view(request):
    # VALIDATE
    serializer = UserAuthenticationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    # AUTHENTICATION
    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    if username and password:
        try:
            token = User.objects.get(username=username)
        except:
            token = Token.objects.create(username=username)
            return Response(data={'key': token.key})
        return  Response(status=status.HTTP_401_UNAUTHORIZED, data={'error': 'User credentials are wrong'})





@api_view(['POST'])
def registration_api_view(request):

    # VALIDATION
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # CREATE USER
    username = serializer.validated_data['username']
    password = serializer.validated_data['password']
    user = User.objects.create_user(username=username, password=password)

    # RETURN RESPONSE
    return Response(status=status.HTTP_201_CREATED, data={'user_id': user.id})