from django.db import models
from django.contrib.auth.models import AbstractUser

 
class User(AbstractUser):
    about = models.TextField(max_length=200)
    profile_image = models.ImageField(upload_to='upload_to')
    

class Chatting(models.Model):
    content = models.CharField(max_length=200, null=True)
    users = models.ForeignKey(User, related_name="chattings", on_delete=models.CASCADE)