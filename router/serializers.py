from rest_framework import serializers

class RouterSerializer(serializers.Serializer):
    json_input = serializers.JSONField
