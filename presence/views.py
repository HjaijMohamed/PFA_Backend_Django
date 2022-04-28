from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser ,MultiPartParser,FormParser
from rest_framework import status
from .method import f_recognition ,f_recognitionOff
from personnels.models import Personnel
from presence.models import Presence
from presence.serializers import PresenceSerializer
from rest_framework.decorators import api_view ,parser_classes


@api_view(['GET', 'POST', 'DELETE'])
@parser_classes([MultiPartParser,FormParser])
def presence_list(request,format=None):
    if request.method == 'GET':
        presences = Presence.objects.all()
        cin = request.query_params.get('cin', None)
        if cin is not None:
            presences = presences.filter(cin__icontains=cin)
        presences_serializer = PresenceSerializer(presences, many=True)
        return JsonResponse(presences_serializer.data, safe=False)
 
    elif request.method == 'POST':
        presence_serializer = PresenceSerializer(data=request.data)
        if presence_serializer.is_valid():
            presence_serializer.save()
            return JsonResponse(presence_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(presence_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Presence.objects.all().delete()
        return JsonResponse({'message': '{} Presences were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 

@api_view(['GET', 'PUT', 'DELETE'])
def presence_detail(request, cin,date): 
    try: 
        presence = Presence.objects.get(cin=cin,date_entree=date)
    except Presence.DoesNotExist: 
        return JsonResponse({'message': 'The presence does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        
    if request.method == 'GET': 
        presence_serializer = PresenceSerializer(presence) 
        return JsonResponse(presence_serializer.data) 
 
    elif request.method == 'PUT': 
        presence_data = JSONParser().parse(request) 
        presence_serializer = PresenceSerializer(presence, data=presence_data) 
        if presence_serializer.is_valid(): 
            presence_serializer.save() 
            return JsonResponse(presence_serializer.data) 
        return JsonResponse(presence_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        presence.delete() 
        return JsonResponse({'message': 'Presence was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def recognition(request):
    if request.method == 'GET':
        personnels=Personnel.objects.all()
        f_recognition(personnels)
        return JsonResponse( status=status.HTTP_201_CREATED)


@api_view(['GET'])
def presence_aujourdhui(request):
    if request.method=='GET':
        sql='select * from presence_presence where date_entree =CAST(CURRENT_TIMESTAMP AS DATE)'
        presences = Presence.objects.raw(sql)
        cin = request.query_params.get('cin', None)
        if cin is not None:
            presences = presences.filter(cin__icontains=cin)
        
        presences_serializer = PresenceSerializer(presences, many=True)
        return JsonResponse(presences_serializer.data, safe=False)


@api_view(['GET'])
def retard_aujourdhui(request):
    if request.method=='GET':
        sql='select * from presence_presence where (date_entree =CAST(CURRENT_TIMESTAMP AS DATE)) and (heure_entree > make_time(8, 15, 23.5))'
        presences = Presence.objects.raw(sql)
        cin = request.query_params.get('cin', None)
        if cin is not None:
            presences = presences.filter(cin__icontains=cin)
        
        presences_serializer = PresenceSerializer(presences, many=True)
        return JsonResponse(presences_serializer.data, safe=False)
