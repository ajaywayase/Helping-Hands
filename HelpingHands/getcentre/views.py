# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sqlite3
from django.shortcuts import render
import urllib.request
from urllib.request import urlopen
import json
import csv
import numpy as np
import pandas as pd
import webbrowser

# Create your views here.

def getcentre(request):
	return render(request, 'getcentre/center.html', {})


def getcentre1(request):
    a = request.POST.get('lat')
    b = request.POST.get('lon')
    lat=a
    lon=b
    s="http://www.google.com/maps?q="+str(lat)+","+str(lon)
    response = urlopen(s)
    a=float((float(a)-18.00)*1000000)
    b=float((float(b)-73.00)*1000000)

    conn = sqlite3.connect('/home/ajay/website/address.db')
    cur = conn.cursor()
    query1 = "Select lat,long from centers"
    print(query1)
    zones = cur.execute(query1)
    zonec = zones.fetchall()
    latitudes = list()
    longitudes = list()
    for i in zonec:
    	if i[0] == 'latitude':
    		pass
    	else:
    		latitudes.append(i[0])
    		longitudes.append(i[1])
    for i in range(0,8):
    	latitudes[i]=latitudes[i]- 18.00
    	longitudes[i]=longitudes[i]- 73.00
    	latitudes[i] = latitudes[i]*1000000
    	longitudes[i] = longitudes[i]*1000000
    	latitudes[i] = latitudes[i] - float(a)
    	longitudes[i] = longitudes[i] - float(b)
    for i in range(0,8):
    	print(latitudes[i],longitudes[i])
    df = pd.DataFrame()
    df['latitude'] = latitudes
    df['longitude'] = longitudes		
    df['latitude'] = df['latitude'] - 18.00
    df['longitude'] = df['longitude'] - 73.00
    df['latitude'] = df['latitude']*1000000
    df['longitude'] = df['longitude']*1000000
    df['latitude'] = df['latitude'] - float(a)
    df['longitude'] = df['longitude'] - float(b)
    df['latitude'] =df['latitude']*df['latitude']
    df['longitude'] =df['longitude']*df['longitude']
    sum = pd.Series()
    sum = df['longitude'] + df['latitude']
    x = sum.idxmin()+1
    print(x)
    return render(request, 'getcentre/map.html', {})
    conn.commit()
    conn.close()
    

	


	
	
	
	
	
	
	
   
    
    
    
    
	
