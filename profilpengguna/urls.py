from django.urls import path
from . import views

app_name = "profilpengguna"

urlpatterns = [
    path('profil/', views.profilPengguna, name='profil-pengguna')
]