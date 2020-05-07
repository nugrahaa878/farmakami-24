from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('apotek/', include('apotek.urls')),
    path('produkapotek/', include('produkapotek.urls')),
    path('transaksipembelian/', include('transaksipembelian.urls')),
    path('profilpengguna/', include('profilpengguna.urls'))
]
