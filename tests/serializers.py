from rest_framework import serializers

from .models import Exercise, ClassRoom


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = ['name', 'difficulty', 'time', 'created_at', 'updated_at']


class ClassRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassRoom
        fields = ['name', 'code', 'exercises', 'created_by', 'members', 'created_at', 'updated_at']
