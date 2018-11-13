from django.shortcuts import render
from blog.models import Post
from blog.serializers import *
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
