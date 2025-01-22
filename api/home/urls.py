from django.urls import path
from .views import (
    HomePageListAPIViews,
    HomePageCreateAPIViews,
    HomePageDetailAPIViews,
    HomePageUpdateAPIViews,
    HomePageDeleteAPIViews
)

urlpatterns = [
    path('', HomePageListAPIViews.as_view(), name='home-list'),           # List all HomePage instances
    path('create/', HomePageCreateAPIViews.as_view(), name='home-create'), # Create a new HomePage instance
    path('<int:pk>/', HomePageDetailAPIViews.as_view(), name='home-detail'), # Retrieve a specific HomePage instance by ID
    path('<int:pk>/update/', HomePageUpdateAPIViews.as_view(), name='home-update'), # Update a specific HomePage instance by ID
    path('<int:pk>/delete/', HomePageDeleteAPIViews.as_view(), name='home-delete'), # Delete a specific HomePage instance by ID
]
