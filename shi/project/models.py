from django.db import models
from media.models import Media
from service.models import Service
from team.models import TeamMember
from modeltranslation.translator import TranslationOptions, translator


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ForeignKey(
        Media, 
        blank=True, 
        null=True, 
        limit_choices_to={'type': 'image'}, 
        on_delete=models.SET_NULL, 
        related_name='project_images'
    )
    hover_image = models.ForeignKey(
        Media, 
        blank=True, 
        null=True, 
        limit_choices_to={'type': 'image'}, 
        on_delete=models.SET_NULL, 
        related_name='project_hover_images'
    )
    project_url = models.URLField(blank=True, null=True)
    project_behance_url = models.URLField(blank=True, null=True)
    year = models.PositiveIntegerField()
    client = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    collaborators = models.ManyToManyField(TeamMember, blank=True, related_name='collaborated_projects')
    services = models.ManyToManyField(Service, blank=True, related_name='projects')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class Badge(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='badges')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
