from django.db import models
from django.contrib.auth.models import AbstractUser , User

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
# class Addfriendlist(models.Model):
#     user = models.OneToOneField(User , on_delete=models.CASCADE)
#     age = models.IntegerField()
#     bio = models.TextField()
#     friend = models.OneToOneField(User , on_delete=models.CASCADE)
#     def __str__(self):
#         return self.user
    
class friendrequest(models.Model):
    name = models.OneToOneField(User , on_delete=models.CASCADE)
    age = models.IntegerField()
    bio = models.TextField()
    friend = models.TextField()
    def __str__(self):
        return self.user
    
