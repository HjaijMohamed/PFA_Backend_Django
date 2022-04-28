from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser ,MultiPartParser,FormParser
from rest_framework import status

from absences.models import Absence
from personnels.models import Personnel
from absences.serializers import AbsenceSerializer
from personnels.serializers import PersonnelSerializer
from rest_framework.decorators import api_view ,parser_classes


@api_view(['GET', 'POST', 'DELETE'])
@parser_classes([MultiPartParser,FormParser])
def absence_list(request,format=None):
    if request.method == 'GET':
        absences = Absence.objects.all()
        cin = request.query_params.get('cin', None)
        if cin is not None:
            absences = absences.filter(cin__icontains=cin)
        
        absences_serializer = AbsenceSerializer(absences, many=True)
        return JsonResponse(absences_serializer.data, safe=False)
 
    elif request.method == 'POST':
        absence_serializer = AbsenceSerializer(data=request.data)
        if absence_serializer.is_valid():
            absence_serializer.save()
            return JsonResponse(absence_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(absence_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Absence.objects.all().delete()
        return JsonResponse({'message': '{} Absence were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def absence_detail(request, pk):
    try: 
        
        absence = Absence.objects.get(pk=pk) 
    except Absence.DoesNotExist: 
        return JsonResponse({'message': 'The Absence does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        absence_serializer = AbsenceSerializer(absence) 
        
        return JsonResponse(absence_serializer.data) 
 
    elif request.method == 'PUT': 
        absence_data = JSONParser().parse(request) 
        absence_serializer = AbsenceSerializer(absence, data=absence_data) 
        if absence_serializer.is_valid(): 
            absence_serializer.save() 
            return JsonResponse(absence_serializer.data) 
        return JsonResponse(absence_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        absence.delete() 
        return JsonResponse({'message': 'Absence was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def absence_aujourdhui(request):
    if request.method=='GET':
        sql='select * from personnels_personnel  where cin not in ((select cin_id from presence_presence  where date_entree =CAST(CURRENT_TIMESTAMP AS DATE)) Union (select cin_id from conges_conge where date_fin >=CAST(CURRENT_TIMESTAMP AS DATE) )) '
        personnels = Personnel.objects.raw(sql)
        cin = request.query_params.get('cin', None)
        if cin is not None:
            personnels = personnels.filter(cin__icontains=cin)
        
        personnels_serializer = PersonnelSerializer(personnels, many=True)
        return JsonResponse(personnels_serializer.data, safe=False)


