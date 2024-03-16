from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Profile_User(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    id_user = models.IntegerField()
    about = models.TextField( null = True, blank = True)
    location = models.CharField(max_length=50, null = True, blank = True)

    def __str__(self):
        return self.user.username