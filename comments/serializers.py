from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id', 'author', 'created_at', 'updated_at', 'project',
            'content',
        ]


class CommentDetailSerializer(CommentSerializer):
    project = serializers.ReadOnlyField(source='project.id')
