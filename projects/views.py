from rest_framework import generics, permissions, filters
from .serializers import ProjectSerializer
from portfolio.permissions import IsOwnerOrReadOnly
from .models import Project
import django_filters.rest_framework


class ProjectList(generics.ListCreateAPIView):
    """
    List projects or create a project if logged in
    """
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Project.objects.all()


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a project, or update or delete it by id if you
    are logged in as admin.
    """
    serializer_class = ProjectSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Project.objects.all()
