from django.db import models

class Comment(models.Model):
    content = models.CharField(max_length=50)
    user = models.ForeignKey("users.User", null=True, related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey("posts.Post", null=True, related_name="comments", on_delete=models.CASCADE)
