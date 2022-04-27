from rest_framework import serializers 
from presence.models import Presence
from personnels.models import Personnel
from personnels.serializers import  PersonnelSerializer

class PresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presence
        fields = ('id',
                  'cin',
                  'date_entree',
                  'heure_entree',
                  'nb_heures',
                 
                  )
