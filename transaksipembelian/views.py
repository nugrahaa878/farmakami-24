from django.shortcuts import render

# Create your views here.
def createTransaksiPembelian(request):
    return render(request, 'create_transaksi_pembelian.html')

def readTransaksiPembelian(request):
    return render(request, 'read_transaksi_pembelian.html')

def updateTransaksiPembelian(request):
    return render(request, 'update_transaksi_pembelian.html')