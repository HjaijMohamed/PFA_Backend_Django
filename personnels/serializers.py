from rest_framework import serializers 
from personnels.models import Personnel
 
 
class PersonnelSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Personnel
        fields = ('cin',
                  'nom',
                  'prenom',
                  'date_nais',
                  'tel',
                  'email',
                  'heure_trav',
                  'img'
                  )