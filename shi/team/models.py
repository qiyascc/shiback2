from django.db import models
from media.models import Media
from django.utils.translation import gettext_lazy as _

class TeamSocial(models.Model):
    team_member = models.ForeignKey('TeamMember', related_name='social_media_accounts', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # Social media name (e.g., Twitter, Facebook)
    url = models.URLField()  # URL of the social media account
    icon = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'type': 'icon'}, related_name="team_social_icon")

    def __str__(self):
        return f"{self.name} ({self.url})"

    class Meta:
        verbose_name = _('Team Social Media')
        verbose_name_plural = _('Team Social Media Accounts')

class TeamMember(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)  # Position (e.g., Founder, Developer)
    image = models.ForeignKey(Media, blank=True, null=True, limit_choices_to={'type': 'image'}, on_delete=models.SET_NULL, related_name="team_member_image")

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['position']

    # Custom method to order 'Founder' position first
    def save(self, *args, **kwargs):
        if self.position.lower() == "founder":
            self.position = "Founder"
        super().save(*args, **kwargs)

class Gallery(models.Model):
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'type': 'image'}, related_name='gallery_images')  # Image from Media with 'image' type
    description = models.TextField(blank=True, null=True)  # Description for the image

    def __str__(self):
        return f"Gallery image {self.id}"

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'