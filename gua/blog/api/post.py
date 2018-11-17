from blog.serializers import PostSerializer
from blog.models import Post

from rest_framework import viewsets, status, permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes


def url_prefix(_url):
    tem = 'api/blog/{url}'
    return tem.format(url=_url)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny, ))
def test_case(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

