from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import BlogPost
from .serializers import BlogPostSerializer
from .permissions import IsOwnerOrReadOnly
from .filters import BlogPostFilter


class BlogPostListCreateView(generics.ListCreateAPIView):

    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]

    filterset_class = BlogPostFilter
    search_fields = ['title', 'content']
    ordering_fields = ['id']
    ordering = ['id']

    def get_queryset(self):
        return BlogPost.objects.filter(
            author=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = BlogPostSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly
    ]

    def get_queryset(self):
        return BlogPost.objects.filter(
            author=self.request.user
        )