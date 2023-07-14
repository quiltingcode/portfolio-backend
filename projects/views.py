from rest_framework import generics, permissions, filters
from .serializers import ProjectSerializer
from portfolio.permissions import IsOwnerOrReadOnly
from .models import Project
from django_filters.rest_framework import DjangoFilterBackend


class ProjectList(generics.ListCreateAPIView):
    """
    List projects or create a project if logged in
    """
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Project.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'tech_stack__name',
    ]


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a project, or update or delete it by id if you
    are logged in as admin.
    """
    serializer_class = ProjectSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Project.objects.all()
