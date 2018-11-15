from django.shortcuts import render
from blog.models import Post
from blog.serializers import *

from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import action


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = JSONParser

    @action(detail=True, methods=['get'])
    def detail(self, request):
        query_key_word = request.query_params.get('query', None)
        if query_key_word == "" or query_key_word is None:
            query_key_word = "all"
        post = Post.objects.filter(title__icontains=query_key_word) if query_key_word != "all" \
            else Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



