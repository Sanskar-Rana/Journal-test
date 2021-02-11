from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm


def registerUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(username=data['username'])
            user.set_password(data['password1'])
            user.save()
            return redirect('/')
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            print(user)
            if user is not None:
                login(request, user)
                return redirect("/home")
            print(data)
    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def logOut(request):
    logout(request)
    return redirect("/")
