from django.db import models         

class Post(models.Mode):
    title = models.CharField(max_length=20)
    content = models.TextField(null=True)
    view_count = models.IntegerField
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)
    attachment = models.FileField( upload_to='MEDIA_ROOT/upload_to', max_length=100)

class Post_Recommend(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)