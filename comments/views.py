from django.shortcuts import render, redirect
from .models import Comment
from posts.models import Post
from django.http import HttpResponse

def comment_create(request, post_id):
        post = Post.objects.get(id=post_id)
        content = request.POST.get("content")

        comment = Comment.objects.create(user=request.user, content = content, post=post)
        comment.save()

        return redirect('post_detail', post_id)
    
def comment_update(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comment = Comment.objects.get(id=comment_id)
    context = {
         'post' : post,
         'comment' : comment
    }
    if request.method == 'POST':
        
        if request.user == comment.user:
            content = request.POST.get('content')

            comment.content = content
            comment.save()

            

            return redirect('post_detail', post_id)
        return HttpResponse("자신의 댓글이 아님")
    else:

        return render(request, 'comment_update.html', context) 


def comment_delete(request, post_id, comment_id):
    comment = Comment.objects.get(id=comment_id)

    if request.user == comment.user:
        comment.delete()
        return redirect('post_detail', post_id)
    
    return HttpResponse("자신의 댓글이 아님")
