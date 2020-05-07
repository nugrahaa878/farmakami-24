from django.shortcuts import render

# Create your views here.
def profilPengguna(request):
    return render(request, 'profil_pengguna.html')