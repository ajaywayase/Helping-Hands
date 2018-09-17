"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import path, include
from django.contrib import admin
from django.urls import path,include
from Home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home.urls')),
    path('sreg/',include('sreg.urls')),
    path('slog/',include('slog.urls')),
    path('wlog/',include('wlog.urls')),
    path('wreg/',include('wreg.urls')),
    path('contact/',include('contact.urls')),
    path('Home/', include('Home.urls')),
    path('getcentre/',include('getcentre.urls')),
   # path('wshow/',include('wshow.urls')),
    #path('sshow/',include('sshow.urls')),
    #path('bookexam/',include('bookexam.urls')),
    #path('userbooked/',include('userbooked.urls')),
]








"""
url(r'^blog/$','www.views.blog',name='blog-index'),
url(r'^blog/posts/$','www.views.blog',name='blog-posts',kwargs={'view_posts': True}),
url(r'^tasks/$','www.views.tasks',name='task-index'),
url(r'^tasks/attachments/$','www.views.tasks',name='task-attachments'),
"""
