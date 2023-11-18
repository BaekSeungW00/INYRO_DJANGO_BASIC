from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse

def post_create(request):
    if request.method == 'GET':
        return render(request, 'post_management.html')
    else:
        title = request.POST.get("title")
        content = request.POST.get("content")
        # file = request.POST.get("file")

        post = Post.objects.create(title = title, content = content)
        post.save()

        post_list = Post.objects.all().order_by('-created_at')
        context = {'post_list': post_list}
        return redirect('post_list')
    


def post_update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user == post.user:
        title = request.POST.get('title')
        content = request.POST.get('content')

        post.title = title
        post.content = content
        post.save()

        return render(request, 'post_detail.html', {'post':post})
    return HttpResponse("자신의 게시물이 아님")


def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.user == post.user:
        post.delete()
        return redirect('post_management.html')
    
    return HttpResponse("자신의 게시물이 아님")

def post_list_view(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list,
    }
    return render(request, 'post_management.html', context)


