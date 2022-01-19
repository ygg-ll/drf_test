"""
因为在 User 模型上'snippets'是反向关系，所以在使用类的时候默认是不包含的ModelSerializer，所以我们需要为它添加一个显式的字段。
"""
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework.viewsets import generics


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
