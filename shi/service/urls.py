from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, ProgressViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'progress', ProgressViewSet, basename='progress')

urlpatterns = router.urls
