from django import http
import rest_framework
from django.http.response import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from icecream import ic
from rest_framework.views import APIView


from tickets.models import Guest

from .serializers import *

# Create your views here.

# Method 1: without REST and no model query FBV:

def no_rest_no_model(request):
    guests = [
        {
            'id':1,
            'name':"Mahmoud",
            'mobile':'01055453213'
        },
        {
            'id':2,
            'name':"Amr",
            'mobile':'010555653213'
        }
    ]

    return JsonResponse(guests ,safe=False)

# Method 2: without REST and with model query FBV:
def no_rest_but_from_model(request):
   data = Guest.objects.all()
   response={
       'guests':list(data.values('name','mobile'))
   }

   return JsonResponse(response)


# Method 3: Fuction Based View
# 3.1 GET POST
@api_view(['GET','POST'])
def FBV_list(request):
    
    # GET:
    if request.method == "GET":
        guests = Guest.objects.all()
        serialzied_data  = GuestSerialzer(guests , many=True)
        return Response(serialzied_data.data)

    # POST:
    elif request.method == "POST":
        serialzier = GuestSerialzer(data=request.data)
        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data , status= status.HTTP_201_CREATED)
        return Response(serialzier.data , status=status.HTTP_400_BAD_REQUEST)


# 3.2 GET PUT DELETE
@api_view(['GET','PUT','DELETE'])
def FBV_pk(request , pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.status.HTTP_404_NOT_FOUND)

    #GET
    if request.method == "GET":
        serializer = GuestSerialzer(guest)
        return Response(serializer.data)
    
    #PUT 
    elif request.method == "PUT":
        serializer = GuestSerialzer(Guest , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    #DELETE 
    elif request.method == "DELETE":
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        











