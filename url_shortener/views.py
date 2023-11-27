from rest_framework import viewsets
from .models import ShrotenedURL
from .serializers import ShortenedURLSerializer
from django.shortcuts import redirect


class ShortenedURLList(viewsets.ModelViewSet):
    queryset = ShrotenedURL.objects.all()
    serializer_class = ShortenedURLSerializer


def redirect_to_original_url(request, short_url):
    shortened_url = ShrotenedURL.objects.get(short_url=short_url)
    return redirect(shortened_url.original_url)
