from django.db import models         

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(null=True)
    view_count = models.IntegerField
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField( upload_to='post_attachment', max_length=100)
    user = models.ForeignKey("users.User", null=True, related_name="posts", on_delete=models.CASCADE)

class Post_Recommend(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", null=True, related_name="post_recommend", on_delete=models.CASCADE)