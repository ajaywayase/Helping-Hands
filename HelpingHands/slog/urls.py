from django.urls import path
from . import views

app_name = 'slog'
urlpatterns = [
    path('', views.logschool, name='logschool'),
    path('wshow/',views.wshow, name='wshow'),
    path('post/',views.post, name='post'),
    path('post1/',views.post1, name='post1'),
    path('vbooked/',views.vbooked, name='vbooked'),
    path('delt/',views.delt, name='delt'),
    path('get10/',views.get10, name='get10'),
]
