from rest_framework import serializers
from .models import Project
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class ProjectSerializer(TaggitSerializer, serializers.ModelSerializer):
    tech_stack = TagListSerializerField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size is larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        return value

    class Meta:
        model = Project
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title', 'description',
            'image', 'tech_stack',
        ]
