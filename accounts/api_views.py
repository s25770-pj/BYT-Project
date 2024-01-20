from django.contrib.auth import authenticate, login, logout, get_user_model
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from django.contrib.auth.views import LoginView
from django.contrib import messages

from accounts.serializers import UserSerializer, LogoutSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class LoginView(LoginView):
    pass


class LogoutView(generics.DestroyAPIView):
    serializer_class = LogoutSerializer
    def post(self, request):
        logout(request)
        return Response("User logged out")


class UserDataView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

