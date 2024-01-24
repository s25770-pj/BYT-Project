from django.contrib.auth import authenticate, login, logout, get_user_model
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView

from accounts.serializers import UserSerializer, LogoutSerializer, RegisterSerializer, GetUserSerializer, \
    ClassSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    authentication_classes = []
    permission_classes = []
    queryset = get_user_model().objects.all()


class LoginView(generics.CreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request,  *args, **kwargs):

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)

            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'detail': 'Login successful.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'detail': 'Invalid login credentials.'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    serializer_class = LogoutSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.auth.delete()
        logout(request)
        return Response({'detail': 'Logout successful.'}, status=status.HTTP_200_OK)


class UserDataView(generics.RetrieveUpdateAPIView):
    serializer_class = GetUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CreateClassView(generics.CreateAPIView):
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

