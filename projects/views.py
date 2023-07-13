from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project


class ProjectList(APIView):
    def get(self, request):
        projects = Project.objects.all()
        return Response(projects)
