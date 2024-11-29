from rest_framework import serializers
from .models import Partner

class PartnerSerializer(serializers.ModelSerializer):
    az = serializers.SerializerMethodField()
    ru = serializers.SerializerMethodField()

    class Meta:
        model = Partner
        fields = ['id', 'name', 'az', 'ru', 'image', 'url']

    def get_az(self, obj):
        return {'name': obj.name_az} if obj.name_az else None

    def get_ru(self, obj):
        return {'name': obj.name_ru} if obj.name_ru else None
