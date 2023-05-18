from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    otp = serializers.CharField(required=False)
    username = serializers.CharField()
    password = serializers.CharField()
