from django.db import models
from django.utils.translation import gettext_lazy as _
from media.models import Media

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=255)  # Service name (translatable)
    title = models.CharField(max_length=255)  # Service title (translatable)
    description = models.TextField()  # Service description (translatable)
    tags = models.ManyToManyField(Tag, related_name='services', null=True, blank=True,)  # Many-to-many relation with tags
    icon = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'type': 'icon'}, related_name="service_icon")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

class Progress(models.Model):
    order = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']  # Order by 'order' field
        verbose_name = "Progress"
        verbose_name_plural = "Progress"