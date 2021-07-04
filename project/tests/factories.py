import factory
from faker import Faker
from app.models import *
fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    
    username = fake.name()
    password = 'password_1'
    first_name = fake.name()
    last_name = "Барнев"

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = "new_post_title"
    content = fake.text()
    user = factory.SubFactory(UserFactory)