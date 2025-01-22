from rest_framework import generics, permissions
from .models import AboutPage
from .serializers import AboutPageSerializer


# class AboutPageViewSet(viewsets.ModelViewSet):
#     """
#         A viewset for viewing and editing AboutPage instances.
#     """
#     queryset = AboutPage.objects.all()
#     serializer_class = AboutPageSerializer
#
#     def get_queryset(self):
#         """
#             Optionally restrict the returned AboutPage to a specific instance.
#         """
#         queryset = AboutPage.objects.all()
#         instance_id = self.request.query_params.get('id', None)
#
#         if instance_id:
#             queryset = queryset.filter(id=instance_id)
#         return queryset

class AboutListAPIView(generics.ListAPIView):

    queryset = AboutPage.objects.all()
    serializer_class = AboutPageSerializer
    permission_classes = [permissions.IsAdminUser]


class AboutCreateAPIView(generics.CreateAPIView):

    queryset = AboutPage.objects.all()
    serializer_class = AboutPageSerializer
    permission_classes = [permissions.IsAdminUser]


class AboutDetailAPIView(generics.RetrieveAPIView):

    queryset = AboutPage.objects.all()
    serializer_class = AboutPageSerializer
    permission_classes = [permissions.AllowAny]


class AboutUpdateAPIView(generics.UpdateAPIView):

    queryset = AboutPage.objects.all()
    serializer_class = AboutPageSerializer
    permission_classes = [permissions.IsAdminUser]


class AboutListAPIView(generics.DestroyAPIView):

    queryset = AboutPage.objects.all()
    serializer_class = AboutPageSerializer
    permission_classes = [permissions.IsAdminUser]
