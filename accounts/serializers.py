from rest_framework import serializers
from django.contrib.auth import get_user_model

from tests.models import ClassRoom


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user


class LogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = self.context['request'].user
        classroom = ClassRoom.objects.create(created_by=user, name=validated_data['name'])
        classroom.users.set([user])
        return classroom

    class Meta:
        model = ClassRoom
        fields = '__all__'
