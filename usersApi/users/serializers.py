from rest_framework import serializers
from .models import MyUser

class MyUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):

        return MyUser.objects.create(**validated_data)