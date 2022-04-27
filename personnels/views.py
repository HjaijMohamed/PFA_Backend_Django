from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser ,MultiPartParser,FormParser
from rest_framework import status
 
from personnels.models import Personnel
from personnels.serializers import PersonnelSerializer
from rest_framework.decorators import api_view ,parser_classes


@api_view(['GET', 'POST', 'DELETE'])
@parser_classes([MultiPartParser,FormParser])
def personnel_list(request,format=None):
    if request.method == 'GET':
        personnels = Personnel.objects.all()
        
        nom = request.query_params.get('nom', None)
        if nom is not None:
            personnels = personnels.filter(nom__icontains=nom)
        
        personnels_serializer = PersonnelSerializer(personnels, many=True)
        return JsonResponse(personnels_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        #personnel_data = FormParser().parse(request)
        personnel_serializer = PersonnelSerializer(data=request.data)
        if personnel_serializer.is_valid():
            personnel_serializer.save()
            return JsonResponse(personnel_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(personnel_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Personnel.objects.all().delete()
        return JsonResponse({'message': '{} Personnels were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def personnel_detail(request, cin):
    try: 
        personnel = Personnel.objects.get(cin=cin) 
    except Personnel.DoesNotExist: 
        return JsonResponse({'message': 'The personnel does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        personnel_serializer = PersonnelSerializer(personnel) 
        return JsonResponse(personnel_serializer.data) 
 
    elif request.method == 'PUT': 
        personnel_data = JSONParser().parse(request) 
        personnel_serializer = PersonnelSerializer(personnel, data=personnel_data) 
        if personnel_serializer.is_valid(): 
            personnel_serializer.save() 
            return JsonResponse(personnel_serializer.data) 
        return JsonResponse(personnel_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        personnel.delete() 
        return JsonResponse({'message': 'Personnel was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
