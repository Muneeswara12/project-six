from django.urls import path
from app1.views import *
app_name='something'
urlpatterns=[
    path('muni1/',muni1,name='muni1')
]