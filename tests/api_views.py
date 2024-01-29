from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Exercise, ClassRoom
from .serializers import ExerciseSerializer, ClassRoomSerializer, CreateClassRoomSerializer


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
    serializer_class = CreateClassRoomSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

