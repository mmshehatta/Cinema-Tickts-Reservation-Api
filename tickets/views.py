from tickets.models import Guest
from django.shortcuts import render
from django.http.response import JsonResponse

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