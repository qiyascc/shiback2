from django.db import models

class CompanyName(models.Model):
    name = models.CharField(max_length=255, default='Shi Studio')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company Name"
        verbose_name_plural = "Company Name"

    def save(self, *args, **kwargs):
        if not self.pk and CompanyName.objects.exists():
            raise ValueError("Only one CompanyName instance is allowed.")
        super().save(*args, **kwargs)


from django.db import models
from media.models import Media

class About(models.Model):
    logo = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'type': 'logo'})
    about_text = models.TextField()
    goal = models.TextField()

    def __str__(self):
        return "About Section"

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Sections"

    def save(self, *args, **kwargs):
        if not self.pk and About.objects.exists():
            raise ValueError("Only one About instance is allowed.")
        super().save(*args, **kwargs)


from django.db import models

class WorkStatus(models.Model):
    members = models.IntegerField()
    completed_projects = models.IntegerField()
    ongoing_projects = models.IntegerField()

    def __str__(self):
        return "Work Status"

    class Meta:
        verbose_name = "Work Status"
        verbose_name_plural = "Work Status"
