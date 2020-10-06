from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'about', 'rank')


class UserExtendedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
