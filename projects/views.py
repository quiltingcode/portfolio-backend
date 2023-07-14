from rest_framework import generics, permissions, filters
from .serializers import ProjectSerializer
from portfolio.permissions import IsOwnerOrReadOnly
from .models import Project


class ProjectList(generics.ListCreateAPIView):
    """
    List events or create an event if logged in
    The perform_create method associates the event with the logged in user.
    """
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an event, or update or delete it by id if you own it.
    """
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
