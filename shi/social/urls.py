from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SocialMediaViewSet

router = DefaultRouter()
router.register(r'social-media', SocialMediaViewSet, basename='social-media')

urlpatterns = router.urls
