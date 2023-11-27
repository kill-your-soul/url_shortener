from django.urls import path, include
from url_shortener.urls import urlpatterns as url_shortener_urls

urlpatterns = [
    path("", include(url_shortener_urls)),
]
