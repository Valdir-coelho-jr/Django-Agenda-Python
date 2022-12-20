from django.shortcuts import render


def login(request):
    return render(request, 'accounts/login.html')


def logiout(request):
    return render(request, 'accounts/logout.html')


def register(request):
    return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
