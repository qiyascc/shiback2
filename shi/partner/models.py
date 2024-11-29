from django.db import models
from media.models import Media

class Partner(models.Model):
    name = models.CharField(max_length=255)
    image = models.ForeignKey(Media, blank=True, null=True, limit_choices_to={'type': 'logo'}, on_delete=models.SET_NULL, related_name="partner_image")
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
