from django.db import models

class Personnel(models.Model):
    cin = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=70, blank=False, default='')
    prenom = models.CharField(max_length=200,blank=False, default='')
    date_nais =models.DateField(blank=True, null=True)
    tel=models.IntegerField(blank=True, null=True)
    email=models.EmailField(default='email@email.com')
    heure_trav=models.TimeField(blank=True, null=True)
    img =models.ImageField(upload_to='images',default='images/inconnu.jpg')