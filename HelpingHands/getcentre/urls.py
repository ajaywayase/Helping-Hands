from django.contrib import admin
from django.urls import path,include
from getcentre import views

app_name = 'getcentre'
urlpatterns = [
    path('', views.getcentre, name='getcentre'),
    path('getcentre1/',views.getcentre1, name='getcentre1')
]
