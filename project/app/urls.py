from django.urls import path
from .views import PostListApiView

urlpatterns = [
    path('posts/list/', PostListApiView.as_view(), name='posts_list')
]