from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Exercise, ClassRoom
from .serializers import ExerciseSerializer, ClassRoomSerializer

from utils.api_views import create_instance


class GetExercisesListApiView(generics.ListAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Exercise.objects.all()


class GetClassRoomsListApiView(generics.ListAPIView):
    serializer_class = ClassRoomSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ClassRoom.objects.all()


class CreateClassView(generics.CreateAPIView):
    serializer_class = ClassRoomSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        if serializer.is_valid():
            validated_data = serializer.validated_data
            return Response(create_instance(serializer, user, validated_data), status=status.HTTP_201_CREATED)


class CreateExerciseApiView(generics.CreateAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        if user and serializer.is_valid():
            validated_data = serializer.validated_data
            return Response(create_instance(serializer, user, validated_data), status=status.HTTP_201_CREATED)
