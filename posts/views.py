from django.shortcuts import render, redirect
from .models import Post

def post_create(request):
    if request.method == 'GET':
        return render(request, 'post_management.html')
    else:
        title = request.POST.get("title")
        content = request.POST.get("content")

        post = Post.objects.create(title = title, content = content)
        post.save()

        post_list = Post.objects.all().order_by('-created_at')
        context = {'post_list': post_list}
        return render(request, 'post_management.html', context)