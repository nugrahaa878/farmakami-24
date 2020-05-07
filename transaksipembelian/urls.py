from django.urls import path
from . import views

app_name = "transaksipembelian"

urlpatterns = [
    path('create_transaksi_pembelian/', views.createTransaksiPembelian, name='create-transaksi-pembelian'),
    path('read_transaksi_pembelian/', views.readTransaksiPembelian, name='read-transaksi-pembelian'),
    path('update_transaksi_pembelian/', views.updateTransaksiPembelian, name='update-transaksi-pembelian')
]