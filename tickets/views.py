from django import http
import rest_framework
from django.http.response import Http404, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from icecream import ic
from rest_framework.views import APIView


from tickets.models import Guest

from .serializers import *

from rest_framework import mixins, generics, viewsets

# Create your views here.

# Method 1: without REST and no model query FBV:


def no_rest_no_model(request):
    guests = [
        {
            'id': 1,
            'name': "Mahmoud",
            'mobile': '01055453213'
        },
        {
            'id': 2,
            'name': "Amr",
            'mobile': '010555653213'
        }
    ]

    return JsonResponse(guests, safe=False)

# Method 2: without REST and with model query FBV:


def no_rest_but_from_model(request):
    data = Guest.objects.all()
    response = {
        'guests': list(data.values('name', 'mobile'))
    }

    return JsonResponse(response)


# Method 3: Fuction Based View
# 3.1 GET POST
@api_view(['GET', 'POST'])
def FBV_list(request):

    # GET:
    if request.method == "GET":
        guests = Guest.objects.all()
        serialzied_data = GuestSerialzer(guests, many=True)
        return Response(serialzied_data.data)

    # POST:
    elif request.method == "POST":
        serialzier = GuestSerialzer(data=request.data)
        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data, status=status.HTTP_201_CREATED)
        return Response(serialzier.data, status=status.HTTP_400_BAD_REQUEST)


# 3.2 GET PUT DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def FBV_pk(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.status.HTTP_404_NOT_FOUND)

    # GET
    if request.method == "GET":
        serializer = GuestSerialzer(guest)
        return Response(serializer.data)

    # PUT
    elif request.method == "PUT":
        serializer = GuestSerialzer(Guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    elif request.method == "DELETE":
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#  Method 4: CBV class based view
# 4.1 list and create ==> GET and POST
class CBV_list(APIView):
    def get(self, request):
        guests = Guest.objects.all()
        serializer = GuestSerialzer(guests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GuestSerialzer(data=request.data)
        ic(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


#  Method 4: CBV_pk class based view
# 4.1 GET PUT DELETE

class CBV_pk(APIView):

    def get_object(self, pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404

    # GET:
    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerialzer(guest)
        return Response(serializer.data)

    # PUT:
    def put(self, request, pk):
        serializer = GuestSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    # DELETE:generics
    def delete(self, request, pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#  Method 5: mixins
#  5.1 mixins list:

class mixin_list(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerialzer

    #Get All objects:
    def get(self , request):
        return self.list(request)
    
    #Create new object:
    def post(self , request):
        return self.create(request)

#  Method 5: mixins
#  5.2 mixins GET PUT DELETE:

class mixins_pk(mixins.RetrieveModelMixin , mixins.UpdateModelMixin,mixins.DestroyModelMixin , generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerialzer()
    
    #GET: 
    def get(self , request , pk):
        return self.retrieve(request)

    #PUT: 
    def put(self , request , pk):
        return self.update(request)

    #DELETE: 
    def delete(self , request , pk):
        return self.destroy(request) 


#  Method 6: generics
#  6.1 list and create ==> GET and POST:
class generics_list(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerialzer

#  6.1 get_pk and update_pk and delete_pk ==> GET PUT DELETE:
class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerialzer

#  Method 7: viewsets
class viewset_guest(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerialzer



# class viewset_movie(viewsets.ModelViewSet):
#     queryset = Guest.objects.all()
#     serializer_class = GuestSerialzer




