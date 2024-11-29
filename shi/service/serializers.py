from rest_framework import serializers
from .models import Service, Tag
from media.models import Media

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class ServiceSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)  # Include the tags in the API response
    icon_url = serializers.SerializerMethodField()  # Display icon URL if available

    class Meta:
        model = Service
        fields = ['id', 'name', 'title', 'description', 'tags', 'icon_url']

    def get_icon_url(self, obj):
        return obj.icon.file.url if obj.icon else None

from rest_framework import serializers
from .models import Progress

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ['order', 'title', 'description']
