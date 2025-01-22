from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TestimonialAPIViewSet


router = DefaultRouter()
router.register(r'', TestimonialAPIViewSet, basename='testimonial')

urlpatterns = [
    path('', include(router.urls))
]
