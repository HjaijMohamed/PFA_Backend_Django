from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser ,MultiPartParser,FormParser
from rest_framework import status

from conges.models import Conge
from conges.serializers import CongeSerializer
from rest_framework.decorators import api_view ,parser_classes


@api_view(['GET', 'POST', 'DELETE'])
@parser_classes([MultiPartParser,FormParser])
def conge_list(request,format=None):
    if request.method == 'GET':
        conges = Conge.objects.all()
        
        cin = request.query_params.get('cin', None)
        if cin is not None:
            conges = conges.filter(cin__icontains=cin)
        
        conges_serializer = CongeSerializer(conges, many=True)
        return JsonResponse(conges_serializer.data, safe=False)
 
    elif request.method == 'POST':
        conge_serializer = CongeSerializer(data=request.data)
        if conge_serializer.is_valid():
            conge_serializer.save()
            return JsonResponse(conge_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(conge_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Conge.objects.all().delete()
        return JsonResponse({'message': '{} Conges were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def conge_detail(request, pk):
    try: 
        conge = Conge.objects.get(pk=pk) 
    except Conge.DoesNotExist: 
        return JsonResponse({'message': 'The Conge does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        conge_serializer = CongeSerializer(conge) 
        return JsonResponse(conge_serializer.data) 
 
    elif request.method == 'PUT': 
        conge_data = JSONParser().parse(request) 
        conge_serializer = CongeSerializer(conge, data=conge_data) 
        if conge_serializer.is_valid(): 
            conge_serializer.save() 
            return JsonResponse(conge_serializer.data) 
        return JsonResponse(conge_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        conge.delete() 
        return JsonResponse({'message': 'Conge was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def conge_aujourdhui(request):
    if request.method=='GET':
        conges = Conge.objects.raw('select * from conges_conge where CAST(CURRENT_TIMESTAMP AS DATE) between date_debut and date_fin')
        cin = request.query_params.get('cin', None)
        if cin is not None:
            conges = conges.filter(cin__icontains=cin)
        
        conges_serializer = CongeSerializer(conges, many=True)
        return JsonResponse(conges_serializer.data, safe=False)
