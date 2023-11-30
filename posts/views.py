from django.shortcuts import render, redirect
from .models import Post, Post_Recommend
from comments.models import Comment
from django.http import HttpResponse

def post_create(request):
    if request.method == 'GET':
        return render(request, 'post_create.html')
    else:
        title = request.POST.get("title")
        content = request.POST.get("content")
        file = request.FILES.get("file")

        post = Post.objects.create(user=request.user, title = title, content = content, attachment=file)
        post.save()

        return redirect('post_detail', post.id)
    


def post_update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        
        if request.user == post.user:
            post.view_count -= 1
            title = request.POST.get('title')
            content = request.POST.get('content')
            file = request.FILES.get("file")

            post.title = title
            post.content = content
            post.file = file
            post.save()

            return redirect('post_detail', post.id)
        return HttpResponse("자신의 게시물이 아님")
    else:
        return render(request, 'post_update.html', {'post':post})


def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.user == post.user:
        post.delete()
        return redirect('post_list')
    
    return HttpResponse("자신의 게시물이 아님")

def post_list_view(request):
    post_list = Post.objects.all().order_by('-created_at')
    context = {
        'post_list': post_list,
    }
    return render(request, 'post_management.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comment = Comment.objects.filter(post_id=post_id)
    is_liked = Post_Recommend.objects.filter(posts=post, user=request.user).exists()

    post.view_count += 1
    post.save()
    context = {
        'post' : post,
        'comment' : comment,
        'is_liked': is_liked
    }
    return render(request, 'post_detail.html', context)


def post_attachment(request, post_id):
    post = Post.objects.get(id=post_id)

    file_path = post.attachment.path
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename={post.attachment.name}'
        return response
    

def like(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user
    post.view_count -= 1

    try:
        recommendation = Post_Recommend.objects.get(posts=post, user=user)
        recommendation.delete()
        post.like_count -= 1
    except Post_Recommend.DoesNotExist:
        Post_Recommend.objects.create(posts=post, user=user)
        post.like_count += 1

    post.save()

    return redirect('post_detail', post_id=post_id)




    
