from glaw.serializers.post import PostSerializer
from glaw.models import Post

from rest_framework import viewsets, status, permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes, parser_classes


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny, ))
@parser_classes((JSONParser,))
def query_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




