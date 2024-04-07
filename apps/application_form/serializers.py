from rest_framework import serializers


class ContactFormSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    message = serializers.CharField()
    telegram = serializers.CharField()
    phone_number = serializers.CharField()
