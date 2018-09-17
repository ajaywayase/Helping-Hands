# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sqlite3
from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'Home/post_list.html', {})

def post_list_about_us(request):
    return render(request, 'Home/post_list.html#info', {})

def post_list_login_section(request):
    return render(request, 'Home/post_list.html#home-heading', {})


