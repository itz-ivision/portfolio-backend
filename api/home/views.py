from rest_framework import generics, permissions
from .models import HomePage
from .serializers import HomePageSerializer


# class HomePageViewSet(viewsets.ModelViewSet):
#
#     queryset = HomePage.objects.all()
#     serializer_class = HomePageSerializer
#
#     def get_queryset(self):
#         queryset = HomePage.objects.all()
#
#         instance_id = self.request.query_params.get('id', None)
#
#         if instance_id:
#             queryset = queryset.filter(id=instance_id)
#         return queryset


class HomePageListAPIViews(generics.ListAPIView):

    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer
    permission_classes = [permissions.IsAdminUser]


class HomePageCreateAPIViews(generics.CreateAPIView):

    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer
    permission_classes = [permissions.IsAdminUser]


class HomePageDetailAPIViews(generics.RetrieveAPIView):

    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer
    permission_classes = [permissions.AllowAny]


class HomePageUpdateAPIViews(generics.UpdateAPIView):

    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer
    permission_classes = [permissions.IsAdminUser]


class HomePageDeleteAPIViews(generics.DestroyAPIView):

    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer
    permission_classes = [permissions.IsAdminUser]

