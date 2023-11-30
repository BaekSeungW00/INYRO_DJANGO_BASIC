from django.shortcuts import render
from django.http import JsonResponse
from .models import Chatting

def chat_view(request):
    if request.method == 'GET':
        messages = Chatting.objects.all()
        return render(request, 'Chatting.html', {'messages': messages})

    elif request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        message = request.POST.get("message")
        user = request.user
        comment = Chatting.objects.create(message=message, user=user)
        # 채팅 추가 후 응답으로 message 반환
        return JsonResponse({'message': comment.message})

    return render(request, 'Chatting.html', {'messages': Chatting.objects.all()})
