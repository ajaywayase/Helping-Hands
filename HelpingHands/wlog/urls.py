from django.urls import path
from . import views

app_name = 'wlog'
urlpatterns = [
    path('', views.logwriter, name='logwriter'),
    path('sshow/',views.sshow, name='sshow'),
    path('userbooked/',views.userbooked, name='userbooked'),
    path('book/',views.book, name='book'),
    path('book1/',views.book1, name='book1'),
    path('delt/',views.delt, name='delt'),
]
