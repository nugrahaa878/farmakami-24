from django.urls import path
from . import views

app_name = "login"

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
