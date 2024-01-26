from django.db import transaction
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


class CreateClassRoomSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        with transaction.atomic():
            try:
                data = self.context['request']
                user = data.get('user')
                classroom = ClassRoom.objects.create(
                    name=validated_data['name'], code=validated_data['code'],
                    created_by=user
                )
                classroom.users = set(user)
                classroom.save()
                return {'response': 'classroom created successfully!', 'classroom': classroom}
            except Exception as ex:
                return {'response': str(ex)}

    class Meta:
        model = ClassRoom
        fields = '__all__'
