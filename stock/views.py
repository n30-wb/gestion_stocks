from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Categorie, Produit
from .forms import CategorieForm, ProduitForm
from django.db.models import Q


# --- VUES POUR LES CATÉGORIES ---

def liste_categories(request):
    """Lister toutes les catégories [cite: 25, 44]"""
    categories = Categorie.objects.all()
    return render(request, 'stock/liste_categories.html', {'categories': categories})


def ajouter_categorie(request):
    """Ajouter une nouvelle catégorie [cite: 24, 45]"""
    if request.method == "POST":
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Catégorie ajoutée avec succès ! ")
            return redirect('liste_categories')
    else:
        form = CategorieForm()
    return render(request, 'stock/ajouter_categorie.html', {'form': form})


def modifier_categorie(request, id):
    """Modifier une catégorie existante [cite: 26, 46]"""
    categorie = get_object_or_404(Categorie, id=id)
    if request.method == "POST":
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            messages.warning(request, "La catégorie a été modifiée. ")
            return redirect('liste_categories')
    else:
        form = CategorieForm(instance=categorie)
    return render(request, 'stock/ajouter_categorie.html', {'form': form})


def supprimer_categorie(request, id):
    """Supprimer une catégorie """
    categorie = get_object_or_404(Categorie, id=id)
    if request.method == "POST":
        categorie.delete()
        messages.error(request, "Catégorie supprimée. ")
        return redirect('liste_categories')
    return render(request, 'stock/confirmer_suppression.html', {'objet': categorie})


# --- VUES POUR LES PRODUITS ---

def liste_produits(request):
    query = request.GET.get('search')
    if query:
        # On filtre si une recherche est tapée
        produits_list = Produit.objects.filter(
            Q(nom__icontains=query) |
            Q(categorie__nom__icontains=query)
        ).order_by('nom')
    else:
        # SINON on affiche tout (c'est ce qui manquait !)
        produits_list = Produit.objects.all().order_by('nom')

    # Garde le reste de ta pagination ici
    paginator = Paginator(produits_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'stock/liste_produits.html', {
        'page_obj': page_obj,
        'search_query': query
    })


def ajouter_produit(request):
    """Ajouter un nouveau produit avec sélection de catégorie [cite: 29, 49]"""
    if request.method == "POST":
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit ajouté avec succès ! ")
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'stock/ajouter_produit.html', {'form': form})