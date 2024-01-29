from rest_framework import serializers
from .models import Exercise, ClassRoom


class CreateClassRoomSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        print(validated_data)
        try:
            user = self.context.get('request').user
            classroom = ClassRoom.objects.create(
                name=validated_data['name'],
                created_by=user
            )
            classroom.members = set(user)
            classroom.save()
            return {'response': 'classroom created successfully!', 'classroom': classroom}
        except Exception as ex:
            return {'response': str(ex)}

    class Meta:
        model = ClassRoom
        fields = ['name', 'code', 'members', 'created_by', 'exercises']


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = ['name', 'difficulty', 'time']


class ClassRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassRoom
        fields = ['name', 'code', 'exercises', 'members']
