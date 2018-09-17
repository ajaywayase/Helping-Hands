# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sqlite3
from django.shortcuts import render

# Create your views here.

def regwriter(request):
    return render(request, 'wreg/regwriter.html', {})

def regwriter1(request):
    global lat,lan
    lat = request.POST.get('lat')
    lon = request.POST.get('long')
    cn = request.POST.get('contact')
    ID = request.POST.get('writerid')
    name = request.POST.get('writername')
    email = request.POST.get('email')
    typ=request.POST.get('type')
    conn = sqlite3.connect('schools.db')
    cur = conn.cursor()
    print("Check1")
    #query1 = "INSERT INTO schools VALUES (:center, :schoolname, :contactNO, :	email)"y
    cur.execute("""INSERT INTO volunteers (cn,ID,type,name,email,lat,long) VALUES (?,?,?,?,?,?,?);""",(cn,ID,typ,name,email,lat,lon))
    tablename="v"+str(ID)
    cur.execute(""" CREATE TABLE """ + tablename + """( ID INTEGER,name TEXT,dat DATE,cn INTEGER,email TEXT,type TEXT);""")
    conn.commit()
    conn.close()
    return render(request, 'wlog/logwriter.html', {})
