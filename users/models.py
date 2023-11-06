from django.db import models
from django.contrib.auth.models import AbstractUser

 
class User(AbstractUser):
    about = models.TextField(max_length=200)
    profile_image = models.ImageField(upload_to='MEDIA_ROOT/upload_to')

class Chatting(models.Model):
    users = models.ForeignKey(User, related_name="chattings")
