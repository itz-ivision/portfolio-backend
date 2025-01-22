from django.urls import path
from .views import (
    ServiceListAPIView,
    ServiceCreateAPIView,
    ServiceDetailAPIView,
    ServiceRetrieveUpdateDestroyAPIView,
    TechnologyListAPIView,
    TechnologyDetailAPIView,
    TechnologyCreateAPIView,
)

urlpatterns = [
    path('', ServiceListAPIView.as_view(), name='service-list'),
    path('create/', ServiceCreateAPIView.as_view(), name='service-create'),
    path('<int:pk>/', ServiceDetailAPIView.as_view(), name='service-detail'),
    path('<int:pk>/edit/', ServiceRetrieveUpdateDestroyAPIView.as_view(), name='service-edit'),

    path('technologies/', TechnologyListAPIView.as_view(), name='technology-list-create'),
    path('technology/create', TechnologyCreateAPIView.as_view(), name='technology-list-create'),
    path('technology/<int:pk>/', TechnologyDetailAPIView.as_view(), name='technology-detail'),
]
