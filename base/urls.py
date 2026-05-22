from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name ='home'),
    path('event/',event,name ='event'),
    path('news/',news,name ='news'),
    path('about/',about,name ='about'),
    path('read/<int:pk>',read,name ='read')
    
]
