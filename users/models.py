from django.db import models
from django.contrib.auth.models import AbstractUser

 
class User(AbstractUser):
    about = models.TextField(max_length=200, null=True)
    profile_image = models.ImageField(upload_to='user_profile_image/', null=True, blank=True)