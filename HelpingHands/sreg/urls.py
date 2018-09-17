from django.urls import path
from . import views

app_name = 'sreg'
urlpatterns = [
    path('', views.regschool, name='regschool'),
    path('/regschool1/',views.regschool1, name='regschool1')
]
