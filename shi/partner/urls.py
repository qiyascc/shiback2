from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PartnerViewSet

router = DefaultRouter()
router.register(r'partners', PartnerViewSet, basename='partner')

urlpatterns = router.urls