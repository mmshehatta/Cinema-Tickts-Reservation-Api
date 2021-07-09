
from django.contrib import admin
from django.urls import path
from tickets import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # method 1:
    path('django/jsonresponse/' ,views.no_rest_no_model),

    # method 2:
    path('django/jsonresponsefrommodel/' ,views.no_rest_but_from_model),
]
