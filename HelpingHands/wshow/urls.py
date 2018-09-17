from django.urls import path
from . import views

app_name = 'wshow'
urlpatterns = [
    path('', views.wshow, name='wshow'),
   
]
