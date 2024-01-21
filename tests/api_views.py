from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Exercise
from .serializers import ExerciseSerializer, ClassRoomSerializer


class GetExercisesListApiView(generics.ListAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Exercise.objects.all()


class GetClassRoomsListApiView(generics.ListAPIView):
    serializer_class = ClassRoomSerializer
    permission_classes = [IsAuthenticated]
