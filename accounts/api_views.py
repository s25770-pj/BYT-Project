from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from .models import KidUser, ParentUser
from .serializers import KidUserSerializer, ParentUserSerializer

from accounts.api_utils.api_client import get_user_details


class KidUserCreateView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = KidUserSerializer(data=request.data)
        if serializer.is_valid():
            user = KidUser.object.create_user(**serializer.validated_data)
            return Response(KidUserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KidUserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        kid_user = authenticate(email=email, password=password)

        if kid_user is not None:
            token, _ = Token.objects.get_or_create(user=kid_user)
            response_data = {'token': token.key, 'message': 'Logged in successfully'}
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class ParentUserCreateView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = ParentUserSerializer(data=request.data)
        if serializer.is_valid():
            user = ParentUser.objects.create_user(**serializer.validated_data)
            return Response(ParentUserSerializer(user).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParentUserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        parent_user = authenticate(email=email, password=password)

        if parent_user is not None:
            token, _ = Token.objects.get_or_create(user=parent_user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserDetailView(APIView):
    def get(self, request):
        user_token = request.session.get('user_token')

        if not user_token:
            return Response({'error': 'Invalid or missing token'}, status=status.HTTP_401_UNAUTHORIZED)

        user_details = get_user_details(user_token)
        if user_details:
            return Response({'message': 'User is authenticated', 'user': user_details})
        else:
            return Response({'error': 'Error occurred while fetching user details'}, status=status.HTTP_400_BAD_REQUEST)
