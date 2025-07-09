from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import SignupForm
from .forms import LoginForm  # Assume you have this
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render

from django.contrib.auth import login as auth_login


def Moreinfo(request):
    return render(request, 'Moreinfo.html')


def Myprofile(request):
    return render(request, 'Myprofile.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Signup successful! Please login.")
            return redirect('login')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def logoutfn(request):
    logout(request)
    return redirect('login')
