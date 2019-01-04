from sepicat.models.user import User
from rest_framework import serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'login',
            'nickname',
        )
