from django.urls import path
from . import views

urlpatterns = [
    # URLs Catégories
    path('categories/', views.liste_categories, name='liste_categories'),
    path('categories/ajouter/', views.ajouter_categorie, name='ajouter_categorie'),
    path('categories/modifier/<int:id>/', views.modifier_categorie, name='modifier_categorie'),
    path('categories/supprimer/<int:id>/', views.supprimer_categorie, name='supprimer_categorie'),

    # URLs Produits
    path('produits/', views.liste_produits, name='liste_produits'),
    path('produits/ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('produits/modifier/<int:id>/', views.modifier_categorie, name='modifier_produit'), # À adapter pour produit
    path('produits/supprimer/<int:id>/', views.supprimer_categorie, name='supprimer_produit'), # À adapter pour produit
]