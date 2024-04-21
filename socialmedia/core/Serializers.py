from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username' , 'email']
        

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = friendrequest
        fileds = '__all__'