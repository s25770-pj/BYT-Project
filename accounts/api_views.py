from django.contrib.auth import authenticate, login, logout, get_user_model
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework.authtoken.models import Token

from accounts.serializers import UserSerializer, LogoutSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class LoginView(generics.CreateAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(generics.DestroyAPIView):
    serializer_class = LogoutSerializer
    def post(self, request):
        logout(request)
        return Response("User logged out")


class UserDataView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

