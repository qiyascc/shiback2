from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from django.http import FileResponse
from .models import Media
from .serializers import MediaSerializer
from django.http import FileResponse
from django.conf import settings
import os

class MediaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']  # name alanına göre filtreleme

    # Türlere göre özel filtreleme endpoint'leri
    @action(detail=False, url_path='icon')
    def icon(self, request):
        queryset = Media.objects.filter(type='icon')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, url_path='gif')
    def gif(self, request):
        queryset = Media.objects.filter(type='gif')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, url_path='video')
    def video(self, request):
        queryset = Media.objects.filter(type='video')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, url_path='image')
    def image(self, request):
        queryset = Media.objects.filter(type='image')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, url_path='logo')
    def logo(self, request):
        queryset = Media.objects.filter(type='logo')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # /media/1/path endpoint'i ekleniyor
    @action(detail=True, url_path='path')
    def file_path(self, request, pk=None):
        media = self.get_object()  # ID'ye göre medya nesnesini al
        file_path = media.file.path  # Dosya yolunu al

        # Dosya var mı kontrol et
        if os.path.exists(file_path):
            # Dosyayı bir yanıt olarak döndür
            return FileResponse(open(file_path, 'rb'), content_type='application/octet-stream')

        # Eğer dosya yoksa 404 döndür
        return Response({"detail": "File not found"}, status=404)
