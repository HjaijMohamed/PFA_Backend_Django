from rest_framework import serializers 
from conges.models import Conge
 
 
class CongeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Conge
        fields = ('id',
                  'cin',
                  'date_debut',
                  'date_fin',
                )