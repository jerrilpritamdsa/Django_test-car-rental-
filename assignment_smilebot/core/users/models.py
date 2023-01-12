from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver

from core import settings

# Create your models here.

class User(AbstractUser):
    is_renter = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    
@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance = None, created  = False, **kwargs):
    if created:
        Token.objects.create(user = instance)

class Renter(models.Model):
    user = models.OneToOneField(User, related_name='renter', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=30, blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
class Owner(models.Model):
    user = models.OneToOneField(User, related_name='owner', on_delete=models.CASCADE)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    
    def __str__(self):
        return self.user.username