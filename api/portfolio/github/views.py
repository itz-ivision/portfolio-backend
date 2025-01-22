from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from .models import GithubRepo
from .serializers import GithubRepoSerializer


class GithubRepoListAPIView(generics.ListAPIView):
    """
        List all GitHub repositories (accessible to everyone).
    """
    queryset = GithubRepo.objects.all()
    serializer_class = GithubRepoSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ['name', 'language']


class GithubRepoDetailAPIView(generics.RetrieveAPIView):
    """
        Retrieve a specific GitHub repository (accessible to everyone).
    """
    queryset = GithubRepo.objects.all()
    serializer_class = GithubRepoSerializer
    permission_classes = [permissions.AllowAny]


class GithubRepoCreateAPIView(generics.CreateAPIView):
    """
        Create a new GitHub repository (admin-only).
    """
    queryset = GithubRepo.objects.all()
    serializer_class = GithubRepoSerializer
    permission_classes = [permissions.IsAdminUser]


class GithubRepoUpdateViewAPI(generics.UpdateAPIView):

    queryset = GithubRepo.objects.all()
    serializer_class = GithubRepoSerializer
    permission_classes = [permissions.IsAdminUser]


class GithubRepoDeleteViewAPI(generics.DestroyAPIView):
    queryset = GithubRepo.objects.all()
    serializer_class = GithubRepoSerializer
    permission_classes = [permissions.IsAdminUser]
