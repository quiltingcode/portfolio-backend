from django.shortcuts import render
from rest_framework import generics, permissions
from portfolio.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment about a project
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you are admin.
    """
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
