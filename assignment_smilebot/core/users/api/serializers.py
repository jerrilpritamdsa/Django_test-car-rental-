from rest_framework import serializers
from users.models import *



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','is_owner']


class RenterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {'input_type':"password"}, write_only = True)
    class Meta:
        model = User
        fields = ['username', 'email','password', 'password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def save(self, **kwargs):
        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email']
        )
        password2 = self.validated_data['password2']
        password = self.validated_data['password']
        if password != password2:
            raise serializers.ValidationError({'error': 'password didnt match'})
        user.set_password(password)
        user.is_renter = True
        user.save()
        Renter.objects.create(user = user)
        return user

class OwnerSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {'input_type':"password"}, write_only = True)
    class Meta:
        model = User
        fields = ['username', 'email','password', 'password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    
    def save(self, **kwargs):
        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email']
        )
        password2 = self.validated_data['password2']
        password = self.validated_data['password']
        if password != password2:
            raise serializers.ValidationError({'error': 'password didnt match'})
        user.set_password(password)
        user.is_owner = True
        user.save()
        Owner.objects.create(user = user)
        return user
        
    