from blog.models import Post
from rest_framework import serializers, viewsets


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'author',
            'body',
        )
