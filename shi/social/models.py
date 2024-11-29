from django.db import models
from media.models import Media

class SocialMedia(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    icon = models.ForeignKey(Media, blank=True, null=True, limit_choices_to={'type': 'icon'}, on_delete=models.SET_NULL, related_name="social_media_icons")

    def __str__(self):
        return self.name


