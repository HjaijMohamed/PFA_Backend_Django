from django.db import models
from personnels.models import Personnel

class Presence(models.Model):
    cin         = models.ForeignKey(Personnel, on_delete=models.CASCADE, null=True)
    date_entree =models.DateField(blank=True, null=True)
    heure_entree=models.TimeField(blank=True, null=True)
    nb_heures    =models.IntegerField(blank=True, null=True)
    class Meta:
        unique_together = (("cin", "date_entree"),)