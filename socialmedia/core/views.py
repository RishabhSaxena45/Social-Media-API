from django.shortcuts import render , HttpResponse , redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics , status
from .models import *
from .Serializers import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout  
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView

# Create your views here.

# class PlayerList(generics.ListAPIView):
#     queryset = Player.objects.all()
#     serializer_class = PlayerSerializer
    

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('upassword')
        user = authenticate(username=username , password=password)
        if user:
            login(request,user)
            return redirect("/user-list")
        else:
            return redirect("/")
    return render(request , 'login.html')

def registerpage(request):
    if request.method=="POST":
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        newuser = User.objects.create_user(username=name , email=email , password=password)
        newuser.save()
        return redirect("/")
    return render(request , 'register.html')


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['username' , 'email']
    
class Friendrequest(generics.ListAPIView):
    queryset = friendrequest.objects.all()
    serializer_class = FriendRequestSerializer
    
