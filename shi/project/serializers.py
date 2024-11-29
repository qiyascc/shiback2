from rest_framework import serializers
from .models import Project, Badge

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ['name']

class ProjectSerializer(serializers.ModelSerializer):
    badges = BadgeSerializer(many=True, read_only=True)
    collaborators = serializers.StringRelatedField(many=True)
    services = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = [
            'id', 'name', 'description', 'image', 'badges', 
            'services', 'project_url', 'project_behance_url',
            'year', 'client', 'industry', 'collaborators'
        ]
