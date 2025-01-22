from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Testimonial
from .serializers import TestimonialSerializer


class TestimonialAPIViewSet(viewsets.ModelViewSet):
    """
        A viewset for viewing, creating, and editing testimonials.
    """
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

    def get_permissions(self):

        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AllowAny]

        return super().get_permissions()