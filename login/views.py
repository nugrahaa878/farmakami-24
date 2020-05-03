from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def welcome(request):
    return render(request, 'welcome.html')

def register(request):
    return render(request, 'register.html')

def adminForm(request):
    return render(request, 'form/admin.html')

def csForm(request):
    return render(request, 'form/cs.html')

def konsumenForm(request):
    return render(request, 'form/konsumen.html')

def kurirForm(request):
    return render(request, 'form/kurir.html')
