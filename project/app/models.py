from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField('Название поста', max_length = 150)
    content = models.CharField('Тело поста', max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.title
