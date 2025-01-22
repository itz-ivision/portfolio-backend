from rest_framework import generics, permissions
from .models import Resume
from .serializers import ResumeSerializer


class ResumeListAPIView(generics.ListAPIView):
    """
        List all resumes (accessible to everyone).
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.AllowAny]


class ResumeDetailAPIView(generics.RetrieveAPIView):
    """
        Retrieve a specific resume (accessible to everyone).
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.AllowAny]


class ResumeCreateAPIView(generics.CreateAPIView):
    """
        Create a new Resume (admin-only).
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAdminUser]


class ResumeUpdateAPIView(generics.UpdateAPIView):
    """
        Create a new Resume (admin-only).
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAdminUser]


class ResumeDeleteAPIView(generics.DestroyAPIView):
    """
        Create a new Resume (admin-only).
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAdminUser]
