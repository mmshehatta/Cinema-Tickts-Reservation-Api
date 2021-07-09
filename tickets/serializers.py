

from django.db.models import fields
from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.ModelSerializerde):
    class Meta:
        model = Movie
        fields = "__all__"

class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields="__all__"


class GuestSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['pk','reservation','name','mobile']