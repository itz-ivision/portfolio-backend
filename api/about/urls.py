from django.urls import path
from .views import (
    AboutListAPIView,
    AboutCreateAPIView,
    AboutDetailAPIView,
    AboutUpdateAPIView,
    AboutListAPIView  # This should be AboutDeleteAPIView instead
)

urlpatterns = [
    path('', AboutListAPIView.as_view(), name='about-list'),
    path('create/', AboutCreateAPIView.as_view(), name='about-create'),
    path('<int:pk>/', AboutDetailAPIView.as_view(), name='about-detail'),
    path('<int:pk>/update/', AboutUpdateAPIView.as_view(), name='about-update'),
    path('<int:pk>/delete/', AboutListAPIView.as_view(), name='about-delete'),
]
