from django.db import models


# Create your models here.
class Client(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    cin = models.CharField(max_length=50)
    permis = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    telephone = models.CharField(max_length=50)


class Vehicule(models.Model):
    matricule = models.IntegerField(null=True, blank=True)
    marque = models.CharField(max_length=50)
    boitVitesse = models.CharField(max_length=20, choices=(('Automatique', 'Automatique'), ('Manuel', 'Manuel')), null=False)
    climatiseur = models.CharField(max_length=20, choices=(('Climatisée', 'Climatisée'), ('N-Climatisée', 'N-Climatisée')), null=False)
    carburant = models.CharField(max_length=20, choices=(('Essence', 'Essence'), ('Gasoil', 'Gasoil'), ('Hybride', 'Hybride')),
                                 null=False)
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='uploads/vehicule', null=True)


class Reservation(models.Model):
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    dateDebut = models.DateField(null=True)
    dateFin = models.DateField(null=True)
    depart = models.CharField(max_length=100)
    retour = models.CharField(max_length=100)


class Blog(models.Model):
    titre = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='uploads/blog')


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=16)
    subject = models.CharField(max_length=200)
    review = models.TextField(blank=True)
