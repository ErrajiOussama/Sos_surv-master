from django.db import models

# Create your models here.
class CLient(models.Model):
    statut = models.CharField(max_length=10,null=True,blank=True)
    Nom = models.CharField(max_length=500,null=True,blank=True)
    Prenom = models.CharField(max_length=500,null=True,blank=True)
    code_Postal = models.CharField(max_length=50,null=True,blank=True)
    adresse=models.CharField(max_length=200,null=True,blank=True)
    Ville=models.CharField(max_length=100,null=True,blank=True)
    E_mail= models.EmailField(null=True,blank=True)
    N_de_téléphone=models.CharField(max_length=200,null=True,blank=True)
    Surface_habitable_m2=models.FloatField(max_length=100,null=True,blank=True)
    facture_d_electricite = models.CharField(max_length=100,null=True,blank=True)
    type_de_toiture = models.CharField(max_length=100,null=True,blank=True)