from django.db import models
import shortuuid

# Create your models here.


class ShrotenedURL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = shortuuid.ShortUUID().random(length=5)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.short_url} - {self.original_url}"
