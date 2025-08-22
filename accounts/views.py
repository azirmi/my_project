from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        messages.error(request, "Hatalı kullanıcı adı veya şifre.")
    return render(request, "login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        password2 = request.POST.get("password2", "")
        key = request.POST.get("key", "")

        if key != "matadorbetmufredat":
            return redirect("login")
        if not username or not password:
            messages.error(request, "Kullanıcı adı ve şifre zorunludur.")
            return redirect("login")
        if password != password2:
            messages.error(request, "Şifreler uyuşmuyor.")
            return redirect("login")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu kullanıcı adı zaten alınmış.")
            return redirect("login")

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Kayıt başarılı! Şimdi giriş yapabilirsiniz.")
        return redirect("login")
    return redirect("login")

@login_required
def dashboard_view(request):
    return render(request, "dashboard.html")

def logout_view(request):
    logout(request)
    messages.info(request, "Çıkış yapıldı.")
    return redirect("login")
