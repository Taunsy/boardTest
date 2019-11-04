from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def signin(request):
    if request.user.is_authenticated:
        error = '로그인 상태다 이말이야'
        return render(request, 'account/loginSuccess.html', {'error': error})
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('/account/loginSuccess/')
        else:
            error = '비밀번호는 8자 이상이다 이말이야'
            return render(request, 'account/signin.html', {'error': error})
    else:
        user_form = UserCreationForm()
        return render(request, 'account/signin.html', {'user_form': user_form})


def login(request):
    if request.user.is_authenticated:
        error = '지랄마라'
        return render(request, 'account/loginSuccess.html', {'error': error})
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('/account/loginSuccess/')
        else:
            error = '이게 아니란 말이다'
            return render(request, 'account/login.html', {'error': error})
    else:
        login_form = AuthenticationForm()
        return render(request, 'account/login.html', {'login_form': login_form})


def logout(request):
    auth_logout(request)
    return redirect('/account/login/')


def loginSuccess(request):
    return render(request, 'account/loginSuccess.html')
