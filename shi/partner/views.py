from rest_framework.viewsets import ModelViewSet
from .models import Partner
from .serializers import PartnerSerializer

class PartnerViewSet(ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
