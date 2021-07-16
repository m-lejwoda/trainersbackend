from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status

@api_view(['GET'])
def index(self):
    return Response({"message": "Hello, world!"})

@api_view(['GET'])
def alltrainershours(request):
    if request.method == 'GET':
        events = Event.objects.filter(date = request.data['date'], trainer = request.data['user'])
        hours = TrainerHoursPerDay.objects.filter(user=request.data['user'])
        serializer = TrainerHoursPerDaySerializer(hours,many=True,context={'allevents': events})
        # serializer = EventsSerializer(events,many=True)
        return Response(serializer.data)

# @api_view(['POST'])
# def trainerhourswithdate(request):
#     if request.method == 'POST':
#         data = request.data
#         data["user"] = request.user.id
#         serializer = TrainerHoursPerDaySerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.data)
