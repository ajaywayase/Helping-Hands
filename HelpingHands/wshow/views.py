# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sqlite3
from django.shortcuts import render
import sqlite3
# Create your views here.

def wshow(request):

	conn = sqlite3.connect('/home/ajay/website/schools.db')
	cur = conn.cursor()
	table_data = cur.execute("select ID,name,email from volunteers")
	return render(request, 'wshow/wshow.html', {"tabless":table_data})
	conn.commit()
	conn.close()
    
	
