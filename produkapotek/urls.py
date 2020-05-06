from django.urls import path
from . import views

app_name = "produkapotek"

urlpatterns = [
    path('create/', views.createProdukApotek, name='create-produk-apotek'),
    path('read/', views.readProdukApotek, name='read-aproduk-apotek'),
    path('update/', views.updateProdukApotek, name='update-produk-apotek')
]
