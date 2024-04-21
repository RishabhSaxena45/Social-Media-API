from django.urls import path
from core.views import *
urlpatterns = [
    # path('player-list/' , PlayerList.as_view()),
    path('' , loginpage),
    path('register/' , registerpage),
    path('user-list/' , UserList.as_view()),
    path('friendrequest/' , Friendrequest.as_view())
]
