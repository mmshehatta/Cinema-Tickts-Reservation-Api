

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def TokenCreate(sender , instance , created , **Kwargs):
    if created:
        Token.objects.create(user=instance)