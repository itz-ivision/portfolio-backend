from django.urls import path
from .views import ChatbotResponseAPIView

urlpatterns = [
    path('', ChatbotResponseAPIView.as_view(), name='chatbot-response'),
]
