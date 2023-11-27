from rest_framework import routers
from django.urls import path, include

from .views import ShortenedURLList, redirect_to_original_url

router = routers.DefaultRouter()
router.register(r"shortened_urls", ShortenedURLList, basename="shortened_urls")

urlpatterns = [
    path("", include(router.urls)),
    path("<str:short_url>/", redirect_to_original_url, name="redirect_to_original_url"),
]
