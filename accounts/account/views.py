from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


def signin(request):
    if request.user.is_authenticated:
        return redirect('')
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('/account/loginSuccess/')
    else:
        user_form = UserCreationForm()
        context = {'user_form': user_form}
        return render(request, 'account/signin.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('')
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('/account/loginSuccess/')
    else:
        login_form = AuthenticationForm()
        context = {'login_form': login_form}
        return render(request, 'account/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('/account/login/')


def loginSuccess(request):
    return render(request, 'account/loginSuccess.html')
