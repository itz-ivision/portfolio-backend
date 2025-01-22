from django.urls import path
from .views import ResumeListAPIView, ResumeDetailAPIView, ResumeCreateAPIView, ResumeUpdateAPIView, ResumeDeleteAPIView


urlpatterns = [
    path('', ResumeListAPIView.as_view(), name='resume-list'),
    path('<int:pk>/', ResumeDetailAPIView.as_view(), name='resume-detail'),
    path('create/', ResumeCreateAPIView.as_view(), name='resume-create'),
    path('update/<int:pk>/', ResumeUpdateAPIView.as_view(), name='resume-update'),
    path('delete/<int:pk>/', ResumeDeleteAPIView.as_view(), name='resume-delete'),
]
