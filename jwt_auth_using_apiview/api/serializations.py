from rest_framework import serializers
from .models import Employee
from django.contrib.auth import get_user_model

User = get_user_model()

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,)
    class Meta:
        model = User
        fields = ('first_name','last_name','username','password','email')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)