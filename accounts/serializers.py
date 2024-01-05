from rest_framework import serializers
from models import KidUser, ParentUser


class KidUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = KidUser
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class ParentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentUser
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
