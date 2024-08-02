from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['username', 'email', 'password']
        

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

class ResetPasswordSerializer(serializers.Serializer):
    new_password=serializers.CharField(write_only=True)
    confirm_password =serializers.CharField(write_only=True)

    def validate(self, data):
        if data['new_password'] !=data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

class LoginSerializer(serializers.Serializer):
    username= serializers.CharField()
    password= serializers.CharField(write_only=True)
