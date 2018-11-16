from blog.serializers import PostSerializer
from blog.models import Post

from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import action


def url_prefix(_url):
    tem = 'blog/{url}'
    return tem.format(url=_url)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # parser_classes = JSONParser

    @action(detail=False, methods=['get'], url_path="oh")
    def detail(self, request):
        query_key_word = request.query_params.get('query', None)
        if query_key_word == "" or query_key_word is None:
            query_key_word = "all"
        post = Post.objects.filter(title__icontains=query_key_word) if query_key_word != "all" \
            else Post.objects.all()
        print(post)
        serializer = PostSerializer(list(post), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


