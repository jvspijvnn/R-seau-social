from django.db import models
from django.contrib.auth import get_user_model
import uuid

# Create your models here.

User = get_user_model()

class Profile_User(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    id_user = models.IntegerField()
    about = models.TextField( null = True, blank = True)
    location = models.CharField(max_length=50, null = True, blank = True)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.user.username

class POST(models.Model):
    user= models.CharField(max_length = 50)
    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    image= models.ImageField(upload_to='images')
    number_of_like = models.PositiveIntegerField(default = 0)

    def __str__(self) -> str:
        return f'{self.user} ({self.id})'

class Comment(models.Model):
    post = models.ForeignKey(POST, on_delete = models.CASCADE, related_name = 'comments')
    content = models.TextField()

class Liked(models.Model):
    post_id = models.CharField(max_length = 500)
    username = models.CharField(max_length = 100)