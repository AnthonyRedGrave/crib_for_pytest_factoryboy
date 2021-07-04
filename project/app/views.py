from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView

class PostListApiView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
