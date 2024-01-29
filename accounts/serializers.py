from django.contrib.auth import get_user_model

from rest_framework import serializers

from tests.models import ClassRoom


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'type']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            type=validated_data['type'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user


class LogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username']


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'type', 'groups']

