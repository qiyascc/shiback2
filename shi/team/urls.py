from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TeamMemberViewSet, GalleryViewSet

router = DefaultRouter()
router.register(r'team-members', TeamMemberViewSet, basename='team-member')
router.register(r'team-members/gallery', GalleryViewSet, basename='gallery')
urlpatterns = router.urls
