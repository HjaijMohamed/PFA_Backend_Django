from django.db import models
from personnels.models import Personnel

class Conge(models.Model):
    cin         = models.ForeignKey(Personnel, on_delete=models.CASCADE, null=True)
    date_debut =models.DateField(blank=True, null=True)
    date_fin=models.DateField(blank=True, null=True)
    class Meta:
        unique_together = (("cin", "date_debut"),)