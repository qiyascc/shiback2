# urls.py

from django.urls import path
from .views import ConstantsAPI

urlpatterns = [
    path('constant/', ConstantsAPI.as_view(), name='constant-api'),
]
