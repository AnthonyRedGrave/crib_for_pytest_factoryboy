import pytest

from app.models import Post
from django.urls import reverse

def test_get_posts_list(db, api_client, post_factory):
    post = post_factory.create_batch(100)
    url = reverse('posts_list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 100

def test_create_post(db, api_client, post_factory):
    post = post_factory()
    url = reverse('posts_detail', kwargs={'pk': post.id})
    response = api_client.get(url)
    assert response.json() == {
        'id': post.id,
        'title': post.title, 
        'content': post.content, 
        'user': post.user.id

    }

