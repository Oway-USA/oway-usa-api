from rest_framework import serializers


class TrackCodeSerializer(serializers.Serializer):
    tracking_number = serializers.CharField()