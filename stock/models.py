from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True) # [cite: 14]
    description = models.TextField(blank=True, null=True) # [cite: 15]

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=100) # [cite: 18]
    description = models.TextField(blank=True, null=True) # [cite: 19]
    prix = models.DecimalField(max_digits=10, decimal_places=2) # [cite: 20]
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE) # [cite: 21]

    def __str__(self):
        return self.nom