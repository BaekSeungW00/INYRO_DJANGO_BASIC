from django.db import models
from users.models import User  # 예시로 User 모델 import

class Chatting(models.Model):
    message = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, null=True, related_name="chattings", on_delete=models.CASCADE)
