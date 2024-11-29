from django.db import models

class Media(models.Model):
    MEDIA_TYPES = [
        ('icon', 'Icon'),
        ('gif', 'Gif'),
        ('video', 'Video'),
        ('image', 'Image'),
        ('logo', 'Logo'),
    ]

    file = models.FileField(upload_to='media_files/')
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=MEDIA_TYPES)

    def __str__(self):
        return f"{self.name} ({self.type})"
