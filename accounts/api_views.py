from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from django.contrib.auth import logout
from .models import Parent, Child
from django.utils.translation import gettext_lazy as _
from rest_framework


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_account_view(request):
    if request.method == 'DELETE':
        user = request.user
        user.delete()
        logout(request)

        message = _('Konto zostało usunięte')
        return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)
    message = _('Nieprawidłowe żądanie')
    return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            message = _('Zalogowano pomyślnie')
            return Response({'message:': message}, status=status.HTTP_200_OK)
    message = _('Błąd logowania')
    return Response({'message': message}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def register_parent_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            message = _('Zarejestrowano pomyślnie')
            return Response({'message': message}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_child_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            parent = request.user
            username = request.data.get('username')
            password = request.data.get('password')

            child = Child(
                parent=parent,
                username=username,
                password=password,
            )
            child.save()
            message = _('Konto dziecka stworzone pomyślnie')
            return Response({'message': message}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    message = _('Nieprawidłowe dane')
    return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)
