from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import TeamMember, Gallery
from .serializers import TeamMemberSerializer, GallerySerializer

class TeamMemberViewSet(ReadOnlyModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class GalleryViewSet(ReadOnlyModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer