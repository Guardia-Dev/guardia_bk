from glaw.models import Post
from rest_framework import serializers, viewsets


class PostSerializer(serializers.ModelSerializer):

    category = serializers.CharField(source='category.name', allow_null=True)
    tag = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'author',
            'body',
            'category',
            'tag',
        )
