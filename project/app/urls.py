from django.urls import path
from .views import PostListApiView, PostRetrieveApiView

urlpatterns = [
    path('posts/', PostListApiView.as_view(), name='posts_list'),
    path('posts/<int:pk>/', PostRetrieveApiView.as_view(), name='posts_detail'),
]