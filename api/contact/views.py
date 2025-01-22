from rest_framework import generics, permissions
from .models import ContactMessage
from .serializers import ContactMessageSerializer
# from .forms import ContactForm


class ContactMessageCreateAPIView(generics.CreateAPIView):
    """
        Create a new contact message.
    """
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]


class ContactMessageListAPIView(generics.ListAPIView):
    """
        List of all contact mess   ages[admin-only]
    """
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.IsAdminUser]


class ContactMessageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        Retrieve, update, or delete a contact message (admin only).
    """
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.IsAdminUser]
