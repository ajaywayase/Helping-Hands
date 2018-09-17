# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sqlite3
from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request, 'contact/contact.html', {})

def Call_Home(request):
	return render(request, 'Home/post_list.html',{})


