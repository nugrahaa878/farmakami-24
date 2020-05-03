from django.urls import path
from . import views

app_name = "login"

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('register/admin', views.adminForm, name="form-admin"),
    path('register/cs', views.csForm, name="form-cs"),
    path('register/konsumen', views.konsumenForm, name="form-konsumen"),
    path('register/kurir', views.kurirForm, name="form-kurir"),
]
