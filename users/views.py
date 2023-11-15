from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("confirm_password")

        if password != password_confirm:
            return redirect('register')
        
        user = User.objects.create_user(username = username, password = password)
        user.save()

        return redirect('login')
    else:
        return render(request, "register.html")
    

    
def login_view(request):
    if request.method =='POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'blog.html', {'user': user})
        else:
            return render(request, 'blog.html', {'user': user})
    else:
        return render(request, 'blog.html', {'user': request.user})
    
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return HttpResponse('로그인 해라 씨발아')



