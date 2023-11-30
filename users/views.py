from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password

def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("confirm_password")
        about = request.POST.get("about")
        profile_image = request.FILES.get("image")

        if password != password_confirm:
            return redirect('register')
        
        user = User.objects.create_user(username = username, password = password, about=about, profile_image=profile_image)
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
        return HttpResponse('로그인 상태가 아닙니다.')


def delete_view(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        pw = request.POST.get('password')
        if check_password(pw, user.password):
            user.delete()
            return redirect('login')
        else:
            return HttpResponse("비밀번호가 틀립니다. ")
    else:
        return render(request, 'check_pw.html')


def profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'profile.html', {'user' : user})
    
    


def profile_update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        if request.user == user:
                about = request.POST.get('about')
                profile_image = request.FILES.get('image')
                print(request.FILES)
                user.about = about
                user.profile_image = profile_image
                user.save()

                return redirect('profile', user.id)
        else:
            return HttpResponse("자신이 아님")
    else:
        return render(request, 'profile_update.html', {'user':user})


def pw_update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        if request.user == user:
                
            password = request.POST.get("password")
            password_confirm = request.POST.get("confirm_password")

            if password != password_confirm:
                return redirect('pw_update')
            if password == user.password:
                return HttpResponse("기존 비밀번호와 같음")
            user.set_password(password)    
            user.save()

            return redirect('login')
        else:
            return HttpResponse("자신이 아님")
    else:
        return render(request, 'update_pw.html', {'user':user})