from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def welcome(request):
    return render(request, 'welcome.html')

def register(request):
    return render(request, 'register.html')