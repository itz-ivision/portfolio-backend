from rest_framework import generics, permissions
from .models import SkillsCategory, Skills
from .serializers import CategorySerializer, SkillSerializer


class CategoryListAPIView(generics.ListAPIView):
    """
        List all categories with their associated skills.
    """
    queryset = SkillsCategory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class SkillsListAPIView(generics.ListAPIView):
    """
        List all Skills
    """
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.AllowAny]


class CategoryCreateAPIView(generics.CreateAPIView):
    """
        Create new Category
    """
    queryset = SkillsCategory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryUpdateAPIView(generics.CreateAPIView):
    """
        Create new Category
    """
    queryset = SkillsCategory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryDeleteAPIView(generics.CreateAPIView):
    """
        Create new Category
    """
    queryset = SkillsCategory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class SkillsCreateAPIView(generics.CreateAPIView):
    """
        Create new Skills
    """
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAdminUser]


class SkillsUpdateAPIView(generics.UpdateAPIView):
    """
        Create new Skills
    """
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAdminUser]


class SkillsDeleteAPIView(generics.DestroyAPIView):
    """
        Create new Skills
    """
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAdminUser]
