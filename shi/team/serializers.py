from rest_framework import serializers, viewsets
from .models import TeamMember, Gallery

class TeamMemberSerializer(serializers.ModelSerializer):
    social_media = serializers.SerializerMethodField()

    class Meta:
        model = TeamMember
        fields = ['id', 'full_name', 'position', 'social_media', 'image']

    def get_social_media(self, obj):
        return [{'name': sm.name, 'icon': sm.icon.file.url if sm.icon else None} for sm in obj.social_media.all()]

# Serializer for the Gallery model
class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'image', 'description']  # Include image and description in the response

