from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from django.contrib.auth import logout
from .models import Parent, Child


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_account_view(request):
    if request.method == 'DELETE':
        user = request.user
        user.delete()
        logout(request)

        return Response({'message': 'Konto zostało usunięte'}, status=status.HTTP_204_NO_CONTENT)
    return Response({'message': 'Nieprawidłowe żądanie'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message:': 'Zalogowano pomyślnie'}, status=status.HTTP_200_OK)
    return Response({'message': ' Błąd logowania'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def register_parent_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response({'message': 'Zarejestrowano pomyślnie'}, status=status.HTTP_200_OK)
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
            return Response({'message': 'Konto dziecka stworzone pomyślnie'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'Nieprawidłowe dane'}, status=status.HTTP_400_BAD_REQUEST)
