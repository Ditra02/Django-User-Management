from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def home(request):
    return render(request=request, template_name='main/home.html')


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request=request, user=user)
            return redirect('/home')

    else:
        form = RegisterForm()

    return render(request=request, template_name='registration/sign_up.html', context={'form': form})
