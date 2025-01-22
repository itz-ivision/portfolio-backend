from django.urls import path
from .views import (
    CertificateDeleteAPIView,
    CertificateListAPIView,
    CertificateCreateAPIView,
    CertificateDetailAPIView,
    CertificateUpdateAPIView,
)

urlpatterns = [
    path('', CertificateListAPIView.as_view(), name='certificate-list'),  # List all certificates
    path('create/', CertificateCreateAPIView.as_view(), name='certificate-create'),  # Create a new certificate
    path('<int:pk>/', CertificateDetailAPIView.as_view(), name='certificate-detail'),  # Retrieve a specific certificate
    path('<int:pk>/update/', CertificateUpdateAPIView.as_view(), name='certificate-update'),  # Update a specific certificate
    path('<int:pk>/delete/', CertificateDeleteAPIView.as_view(), name='certificate-update'),  # Update a specific certificate
]
