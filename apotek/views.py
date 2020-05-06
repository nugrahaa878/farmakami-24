from django.shortcuts import render

# Create your views here.

def createApotek(request):
    return render(request, 'create_apotek.html')

def readApotek(request):
    return render(request, 'read_apotek.html')

def updateApotek(request):
    return render(request, 'update_apotek.html')
