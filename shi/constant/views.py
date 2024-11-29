# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from company.models import About, CompanyName, WorkStatus
from media.models import Media
from partner.models import Partner as Partnership
from project.models import Project as Work
from service.models import Tag, Service, Progress
from service.models import Progress as HoverableItem
from social.models import SocialMedia


from media.serializers import MediaSerializer
from company.serializers import CompanyNameSerializer, AboutSerializer, WorkStatusSerializer
from service.serializers import ServiceSerializer
from partner.serializers import PartnerSerializer
from social.serializers import SocialMediaSerializer
from project.serializers import ProjectSerializer as WorkSerializer
from service.serializers import ProgressSerializer as HoverableItemSerializer

class ConstantsAPI(APIView):
    def get(self, request, format=None):
        partnerships = Partnership.objects.all()
        services = Service.objects.all()
        social_media = SocialMedia.objects.all()
        works = Work.objects.all()
        hoverable_items = HoverableItem.objects.all()

        partnership_serializer = PartnerSerializer(partnerships, many=True)
        service_serializer = ServiceSerializer(services, many=True)
        social_media_serializer = SocialMediaSerializer(social_media, many=True)
        work_serializer = WorkSerializer(works, many=True)
        hoverable_item_serializer = HoverableItemSerializer(hoverable_items, many=True)

        data = {
            'partnershipsList': partnership_serializer.data,
            'ourServicesList': service_serializer.data,
            'socialMediaList': social_media_serializer.data,
            'works': work_serializer.data,
            'hoverableItems': hoverable_item_serializer.data,
        }

        return Response(data)
