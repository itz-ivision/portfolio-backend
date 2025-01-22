from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from .models import BlogCategory, BlogPost, Tag
from .serializers import CategorySerializer, BlogPostSerializer, TagSerializer


# class CategoryViewSet(viewsets.ModelViewSet):
#     """
#         A view-set for viewing and editing Category instances.
#     """
#     queryset = BlogCategory.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [permissions.IsAdminUser]
#

class CategoryListAPIView(generics.ListAPIView):

    queryset = BlogCategory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryCreateAPIView(generics.CreateAPIView):

    queryset = BlogCategory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = BlogCategory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class BlogListAPIView(generics.ListAPIView):

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ['tags__name']


class BlogCreateAPIView(generics.CreateAPIView):

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAdminUser]


# class BlogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer
#     permission_classes = [permissions.IsAdminUser]
#

class BlogDetailAPIView(generics.RetrieveAPIView):

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]


class BlogUpdateAPIView(generics.UpdateAPIView):

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAdminUser]


class BlogDeleteAPIView(generics.DestroyAPIView):

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAdminUser]


# class BlogPostViewSet(viewsets.ModelViewSet):
#     """
#         A view-set for viewing and editing BlogPost instances.
#     """
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer
#     permission_classes = [permissions.IsAdminUser]
#
#     def get_queryset(self):
#         """
#             Optionally restrict the returned BlogPost to those by a specific author.
#         """
#         queryset = BlogPost.objects.all()
#         author = self.request.query_params.get('author', None)
#
#         if author:
#             queryset = queryset.filter(author_id=author)
#
#         return queryset


# class TagViewSet(viewsets.ModelViewSet):
#     """
#         A view-set for viewing and editing Tag instances.
#     """
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#     permission_classes = [permissions.IsAdminUser]


class TagListAPIView(generics.ListAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAdminUser]


class TagCreateAPIView(generics.CreateAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAdminUser]


class TagRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAdminUser]
