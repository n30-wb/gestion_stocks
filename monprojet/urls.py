from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView # Importe ceci

urlpatterns = [
    path('admin/', admin.site.urls),
    # Redirige la page d'accueil vers la liste des catégories
    path('', RedirectView.as_view(url='categories/', permanent=True)),
    path('', include('stock.urls')),
]