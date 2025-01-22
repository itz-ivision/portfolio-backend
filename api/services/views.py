from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from .models import Technology, Service
from .serializers import TechnologySerializer, ServiceSerializer


class ServiceListAPIView(generics.ListAPIView):
    """
        GET: List all services.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ['technologies__name']


class ServiceCreateAPIView(generics.CreateAPIView):
    """
        POST: Create new service.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAdminUser]


class ServiceDetailAPIView(generics.RetrieveAPIView):
    """
        GET: Retrieve a service by ID.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


class ServiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        GET: Retrieve a service by ID.
        PUT: Update a service by ID.
        DELETE: Delete a service by ID.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAdminUser]


class TechnologyListAPIView(generics.ListAPIView):
    """
        GET: List all technologies.
    """
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [permissions.AllowAny]

class TechnologyCreateAPIView(generics.CreateAPIView):
    """
        POST: Create new technology.
    """
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [permissions.IsAdminUser]

class TechnologyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        GET: Retrieve a technology by ID.
        PUT: Update a technology by ID.
        DELETE: Delete a technology by ID.
    """
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [permissions.IsAdminUser]
