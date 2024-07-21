from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_page(request):
    if request.user.is_authenticated:
        return redirect('app:index')
    return render(request, "login.html")

@require_POST
def logins(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    if username is None:
        print("username")
        return redirect("auth:login")
    
    if password is None:
        print("password")
        return redirect("auth:login")
    
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect("app:index")
    
    print("username yoki password xato")
    return redirect("auth:login")

@login_required(login_url="auth:login")
def logout_page(request):
    logout(request)
    return redirect("auth:login")
