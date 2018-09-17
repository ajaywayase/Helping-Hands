from django.urls import path,include
from . import views

app_name = 'Home'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('', views.post_list_about_us, name='post_list_about_us'),
    path('', views.post_list_login_section, name='post_list_login_section'),
    #path(r'^post_list/','sreg.urls'),
    
]


