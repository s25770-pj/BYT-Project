from rest_framework import serializers
from .models import Exercise, ClassRoom


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = '__all__'


class ClassRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassRoom
        fields = '__all__'
