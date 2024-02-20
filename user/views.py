from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import check_password


# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data["name"]
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        
        all_users = User.objects.filter(username = username)

        if len(all_users) > 0:
            messages.warning(request, 'Kullanıcı adı zaten kullanılıyor.')
        
        new_user = User.objects.create(username = username, email = email, first_name = name)
        new_user.set_password(password)
        new_user.save()
        login(request, new_user)
        messages.success(request, "Başarıyla kayıt oldunuz")

        return redirect("main_page")
    
    return render(request, "register.html", {"form": form})

def login_user(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']

        print(password)

        user = User.objects.filter(username = username).first()

        if user:
            if check_password(user.password, password):
                print("aferim")

        user = authenticate(request, username = username, password = password, email = email)

        if user is not None:
            login(request, user)
            messages.success(request, "Başarıyla giriş yaptınız")

            return redirect("main_page")
        else:

            messages.warning(request, "Kullanıcı adı veya şifre hatalı")
            return redirect("login")
        
        
    
    return render(request, "login.html", {"form": form})

def logout_user(request):
    logout(request)
    messages.success(request, "Başarıyla çıkış yaptınız")

    return redirect("main_page")

