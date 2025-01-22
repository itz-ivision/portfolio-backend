from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Certificate
from .serializers import CertificateSerializer


class CertificateListAPIView(generics.ListAPIView):
    """
    Handles listing all certificates (GET).
    - Accessible to any user.
    """
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [AllowAny]  # Anyone can list certificates


class CertificateCreateAPIView(generics.CreateAPIView):
    """
    Handles creating a new certificate (POST).
    - Accessible only to admin users.
    """
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAdminUser]  # Only admins can create certificates


class CertificateDetailAPIView(generics.RetrieveAPIView):
    """
    Handles retrieving a specific certificate (GET).
    - Accessible to any user.
    """
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [AllowAny]  # Anyone can retrieve certificate details


class CertificateUpdateAPIView(generics.UpdateAPIView):
    """
    Handles updating a certificate (PUT or PATCH).
    - Accessible only to admin users.
    """
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAdminUser]  # Only admins can update certificates


class CertificateDeleteAPIView(generics.DestroyAPIView):
    """
    Handles deleting a specific certificate (DELETE).
    - Accessible only to admin users.
    """
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAdminUser]