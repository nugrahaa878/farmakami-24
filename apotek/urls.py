from django.urls import path
from . import views

app_name = "apotek"

urlpatterns = [
    path('create/', views.createApotek, name='create-apotek'),
    path('read/', views.readApotek, name='read-apotek'),
    path('update/', views.updateApotek, name='update-apotek')
]
