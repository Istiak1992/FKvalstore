from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    

    class Meta:
        fields = '__all__'
        model = User


class TestSerializer(serializers.ModelSerializer):
    name = UserSerializer(many=False, read_only=True)
    name_id = serializers.IntegerField(write_only=True)

    class Meta:
        fields = '__all__'
        model = Test