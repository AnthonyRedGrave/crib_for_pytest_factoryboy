import pytest

from app.models import Post
from django.urls import reverse

def test_get_posts_list(db, api_client, post_factory):
    post = post_factory()
    url = reverse('posts_list')
    response = api_client.get(url)
    print(response.json())
    assert response.status_code == 200
    assert response.json() == [
        {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'user': post.user.id
        }
    ]

# def test_new_post_factory(db, post_factory):
#     post = post_factory.create()
#     print(post.user.__dict__)
#     assert True
