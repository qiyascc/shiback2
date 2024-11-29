from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CompanyNameViewSet, AboutViewSet, WorkStatusViewSet

router = DefaultRouter()
router.register(r'company-name', CompanyNameViewSet, basename='company-name')
router.register(r'about', AboutViewSet, basename='about')
router.register(r'work-status', WorkStatusViewSet, basename='work-status')

urlpatterns = router.urls
