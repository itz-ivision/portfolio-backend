from django.urls import path
from .views import ContactMessageCreateAPIView, ContactMessageListAPIView, ContactMessageDetailAPIView


urlpatterns = [
    path('create/', ContactMessageCreateAPIView.as_view(), name='contact-create'),
    path('list/', ContactMessageListAPIView.as_view(), name='contact-list'),
    path('<int:pk>/', ContactMessageDetailAPIView.as_view(), name='contact-detail'),
]
