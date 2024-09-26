

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer, LoginSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
User = get_user_model()

@api_view(['POST'])
def register_user(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'message': 'User registered. Check your email for confirmation code.', 'confirmation_code': user.confirmation_code}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def confirm_user(request):
    code = request.data.get('confirmation_code')
    username = request.data.get('username')

    if not code or not username:
        return Response({'error': 'Confirmation code and username are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    if user.confirmation_code == code:
        user.is_active = True
        user.confirmation_code = None  # Удаляем код подтверждения после успешной активации
        user.save()
        return Response({'message': 'User confirmed successfully.'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid confirmation code.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterUserView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    'message': 'User registered. Check your email for confirmation code.',
                    'confirmation_code': user.confirmation_code
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConfirmUserView(APIView):
    def post(self, request):
        code = request.data.get('confirmation_code')
        username = request.data.get('username')

        if not code or not username:
            return Response({'error': 'Confirmation code and username are required.'}, status=status.HTTP_400_BAD_REQUEST)

        User = get_user_model()
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        if user.confirmation_code == code:
            user.is_active = True
            user.confirmation_code = None  # Удаляем код подтверждения после успешной активации
            user.save()
            return Response({'message': 'User confirmed successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid confirmation code.'}, status=status.HTTP_400_BAD_REQUEST)

class LoginUserView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
