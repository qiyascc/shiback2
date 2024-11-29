from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Service
from .serializers import ServiceSerializer

class ServiceViewSet(ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Progress
from .serializers import ProgressSerializer

class ProgressViewSet(ReadOnlyModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
