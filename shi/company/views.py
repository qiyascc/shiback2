from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import CompanyName, About, WorkStatus
from .serializers import CompanyNameSerializer, AboutSerializer, WorkStatusSerializer
# Create your views here.
# CompanyName API ViewSet
class CompanyNameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CompanyName.objects.all()
    serializer_class = CompanyNameSerializer


# About API ViewSet
class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


# WorkStatus API ViewSet
class WorkStatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WorkStatus.objects.all()
    serializer_class = WorkStatusSerializer