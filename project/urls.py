
from django.contrib import admin
from django.urls import path , include
from tickets import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("guests" , views.viewset_guest)
router.register("movies" , views.viewset_movie)
router.register("reservs" , views.viewset_reservation)

urlpatterns = [
    path('admin/', admin.site.urls),
    # method 1:
    path('django/jsonresponse/' ,views.no_rest_no_model),

    # method 2:
    path('django/jsonresponsefrommodel/' ,views.no_rest_but_from_model),
   
    # method 3.1: GET and POST from rest framework FBV @api_view
    path('rest/fbv/' ,views.FBV_list),

    # method 3.2:GET PUT DELETE  from restframework FBV @api_view
    path('rest/fbv/<int:pk>' ,views.FBV_pk),

     # method 4.1: GET and POST from rest framework CBV APIView class
    path('rest/cbv/' ,views.CBV_list.as_view()),

    # method 4.2:GET PUT DELETE from rest framework CBV APIView class
    path('rest/mixins/<int:pk>' ,views.CBV_pk.as_view()),

    # method 5.1:GET and POST from rest framework by mixins
    path('rest/mixins/' ,views.mixin_list.as_view()),

    # method 5.1:GET PUT DELETE from rest framework by mixins
    path('rest/mixins/<int:pk>' ,views.mixins_pk.as_view()),
  
    # method 6.1:GET and POST from rest framework by Generics
    path('rest/generics/' ,views.generics_list.as_view()),

    # method 6.1:GET PUT DELETE from rest framework by Generics
    path('rest/generics/<int:pk>' ,views.generics_pk.as_view()),
    
    # method 7 :rest framework by viewsets
    path('rest/viewset/' , include(router.urls)),
    
    
    # some business logics
    # search for movie by hall or name
    path('fbv/findmovie' , views.find_movie),

    # add new Reservation:
    path('fbv/newres' , views.new_reserv),





]
