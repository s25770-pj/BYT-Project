import re
from rest_framework import serializers


class RegistrationSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=50, min_length=8)
    password = serializers.CharField(max_length=50, min_length=8)
    email = serializers.CharField(max_length=100, min_length=8)

    @staticmethod
    def validate_login(data):
        if len(data) < 8:
            raise serializers.ValidationError('Login musi składac sie z conajmniej 8 znaków')

        if len(data) > 50:
            raise serializers.ValidationError('Login nie może składac sie z wiecej niz 50 znaków')

        if any(char in '!@#$%^&*()[]' for char in data):
            raise serializers.ValidationError('Login nie może zawierać znaków specjalnych')
        return data

    @staticmethod
    def validate_password(data):
        if len(data) < 8:
            raise serializers.ValidationError('Hasło musi składac sie z conajmniej 8 znaków')

        if len(data) > 50:
            raise serializers.ValidationError('Hasło nie może składac sie z więcej niz 50 znaków')

        if not any(char in '!@#$%^&*()[]' for char in data):
            raise serializers.ValidationError('Hasło musi zawierać znaki specjalne')
        return data

    @staticmethod
    def validate_email(data):
        if len(data) > 255:
            raise serializers.ValidationError('Email nie może składac sie z wiecej niz 255 znaków')

        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, data):
            raise serializers.ValidationError('Nieprawidłowy adres email')
        return data
