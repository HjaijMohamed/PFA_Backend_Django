from django.db import models
from personnels.models import Personnel

class Absence(models.Model):
    cin         = models.ForeignKey(Personnel, on_delete=models.CASCADE, null=True)
    date_absence =models.DateField(blank=True, null=True)
    class Meta:
        unique_together = (("cin", "date_absence"),)