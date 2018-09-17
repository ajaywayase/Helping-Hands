from django.urls import path
from . import views

app_name = 'wreg'
urlpatterns = [
    path('', views.regwriter, name='regwriter'),
    path('/regwriter1/',views.regwriter1, name='regwriter1')
]
