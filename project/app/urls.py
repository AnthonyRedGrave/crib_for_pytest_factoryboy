from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('posts/list/view/', PostListApiView.as_view(), name='posts_list'),
    path('posts/<int:pk>/', PostRetrieveApiView.as_view(), name='posts_detail'),
]

urlpatterns += router.urls