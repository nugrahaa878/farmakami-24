from django.shortcuts import render

def createProdukApotek(request):
    return render(request, 'create_produk_apotek.html')

def readProdukApotek(request):
    return render(request, 'read_produk_apotek.html')

def updateProdukApotek(request):
    return render(request, 'update_produk_apotek.html')
