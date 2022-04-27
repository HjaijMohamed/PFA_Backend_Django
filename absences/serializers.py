from rest_framework import serializers 
from absences.models import Absence
 
 
class AbsenceSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Absence
        fields = ('id',
                  'cin',
                  'date_absence'
                )