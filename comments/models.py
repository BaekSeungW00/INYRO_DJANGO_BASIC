from django.db import models

class Comment(models.Model):
    content = models.TextField(max_length=50)

class CommentLike(models.Model):
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)

class Reply(models.Model):
    content = models.TextField(max_length=50)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)