from django.urls import path
from .views import (
    CategoryListAPIView,
    CategoryCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    BlogListAPIView,
    BlogCreateAPIView,
    BlogDetailAPIView,
    BlogUpdateAPIView,
    BlogDeleteAPIView,
    TagListAPIView,
    TagCreateAPIView,
    TagRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),

    path('posts/', BlogListAPIView.as_view(), name='blog-list'),
    path('post/create/', BlogCreateAPIView.as_view(), name='blog-create'),
    path('post/<int:pk>/', BlogDetailAPIView.as_view(), name='blog-detail'),
    path('post/update/<int:pk>/', BlogUpdateAPIView.as_view(), name='blog-detail'),
    path('post/delete/<int:pk>/', BlogDeleteAPIView.as_view(), name='blog-detail'),

    path('tags/', TagListAPIView.as_view(), name='tag-list'),
    path('tags/create/', TagCreateAPIView.as_view(), name='tag-create'),
    path('tags/<int:pk>/', TagRetrieveUpdateDestroyAPIView.as_view(), name='tag-detail'),
]
