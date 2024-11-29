from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import SocialMedia
from .serializers import SocialMediaSerializer

class SocialMediaViewSet(ReadOnlyModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
