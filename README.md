# 🚀 GestionStock - Catalogue Pro Vibrant 📦

Une application de gestion de stock moderne et ultra-visuelle développée avec **Django 5**. Ce projet transforme une interface d'inventaire classique en une galerie interactive "Vibrant Design" inspirée des standards du web actuel.

---

## ✨ Fonctionnalités Clés

- 🎨 **UI/UX Spectaculaire** : 
  - Design en "Cards" (cartes) interactives.
  - Dégradés de couleurs vifs (Cyan, Magenta, Indigo).
  - Effets de survol (hover) avec élévation et ombres portées.
  - Typographie moderne (Plus Jakarta Sans).

- 📋 **Gestion Complète (CRUD)** :
  - **Produits** : Ajout, modification, suppression et affichage détaillé.
  - **Catégories** : Organisation par familles avec dossiers visuels.

- 🔍 **Bonus Intégrés** :
  - **Recherche Intelligente** : Filtrage dynamique des produits par nom ou par catégorie.
  - **Pagination Fluide** : Navigation optimisée pour les catalogues volumineux (5 éléments par page).
  - **Animations** : Transitions fluides au chargement des pages (Animate.css).

---

## 🛠️ Installation & Lancement Rapide

Suivez ces étapes pour exécuter le projet sur votre machine locale :

### 1. Cloner le dépôt
```bash
git clone [https://github.com/VOTRE_PSEUDO/gestion_stock.git](https://github.com/VOTRE_PSEUDO/gestion_stock.git)
cd gestion_stock
Configurer l'environnement virtuel
Bash
python -m venv venv

# Activation (Windows)
venv\Scripts\activate

# Activation (Mac/Linux)
source venv/bin/activate

Installer les dépendances

Bash
pip install -r requirements.txt

initialiser la base de données

Bash
python manage.py migrate

Lancer le serveur
Bash
python manage.py runserver 9000