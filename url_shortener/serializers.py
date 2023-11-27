from rest_framework import serializers
from .models import ShrotenedURL


class ShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShrotenedURL
        fields = ["original_url", "short_url"]
