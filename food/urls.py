'''specific url mapping for app1'''
from django.urls import path
from food.views import *
app_name='food'
urlpatterns=[
    path('eatfit/',eatfit,name='eatfit'),
]