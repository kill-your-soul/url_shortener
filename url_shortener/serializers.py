from rest_framework import serializers
from .models import ShrotenedURL


class ShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShrotenedURL
        fields = ["original_url", "short_url"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["short_url"] = self.context["request"].build_absolute_uri(
            f"/api/{data['short_url']}"
        )
        return data
