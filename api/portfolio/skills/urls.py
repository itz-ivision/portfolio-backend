from django.urls import path
from .views import (SkillsListAPIView,
                    SkillsCreateAPIView,
                    CategoryListAPIView,
                    CategoryCreateAPIView,
                    CategoryUpdateAPIView,
                    CategoryDeleteAPIView,
                    SkillsUpdateAPIView,
                    SkillsDeleteAPIView)


urlpatterns = [
    path('', SkillsListAPIView.as_view(), name='skills-list'),
    path('create/', SkillsCreateAPIView.as_view(), name='skills-create'),
    path('update/<int:pk>/', SkillsUpdateAPIView.as_view(), name='skills-update'),
    path('delete/<int:pk>/', SkillsDeleteAPIView.as_view(), name='skills-delete'),
    path('categories/', CategoryListAPIView.as_view(), name='skills-categories-list'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='skills-category-create'),
    path('category/update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='skills-category-update'),
    path('category/delete/<int:pk>/', CategoryDeleteAPIView.as_view(), name='skills-category-delete'),
]
