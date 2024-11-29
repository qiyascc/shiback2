from rest_framework import serializers, viewsets
from .models import CompanyName, About, WorkStatus

# CompanyName Serializer
class CompanyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyName
        fields = ['name']


# About Serializer
class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['logo', 'about_text', 'goal']


# WorkStatus Serializer
class WorkStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkStatus
        fields = ['members', 'completed_projects', 'ongoing_projects']



