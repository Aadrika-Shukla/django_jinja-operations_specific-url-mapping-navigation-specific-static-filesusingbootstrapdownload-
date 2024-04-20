'''specific url mapping for app1'''
from django.urls import path
from travel.views import *
app_name='travel'
urlpatterns=[
    path('world/',world,name='world'),
]