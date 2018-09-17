# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sqlite3
from django.shortcuts import render
import numpy as np
import pandas as pd
# Create your views here.

def logschool(request):
    	return render(request, 'slog/logschool.html', {})

def wshow(request):
	try:
		global sid
		sid=request.POST.get("sid")
		conn = sqlite3.connect('/home/suraj/Documents/website/schools.db')
		cur = conn.cursor()
		query1 = "Select ID,name,type,cn,email from volunteers;"		#returns tuple of lat and long
		print(query1)
		ps = cur.execute(query1)
		pc = ps.fetchall()
		query1 = "Select ID,name,type,cn,email from volunteers ORDER BY type;"
		print(query1)
		ps1 = cur.execute(query1)
		pc1 = ps.fetchall()
		query1 = "Select ID,name,type,cn,email from volunteers ORDER BY name;"
		print(query1)
		ps2 = cur.execute(query1)
		pc2 = ps.fetchall()
		
		if sid is None:
			return render(request, 'slog/logschool.html', {})
		return render(request, 'slog/wshow.html', {"tabless1":pc,"tabless2":pc1,"tabless3":pc2})
		conn.commit()
		conn.close()
	except:
		return render(request, 'slog/logschool.html', { })
def post(request):
	return render(request, 'slog/post.html', {})
  
def post1(request):
	try:
		dat=request.POST.get('date')
		#sn=request.POST.get('sid')
		lat=request.POST.get('lat')
		typ=request.POST.get('type')
		lon=request.POST.get('long')
		conn = sqlite3.connect('schools.db')
		cur = conn.cursor()
		if sid is None:
			return render(request, 'slog/logschool.html', { })
		exms=cur.execute("""SELECT * FROM schools WHERE schools.ID= """+ sid +""";""")
		exmc = exms.fetchall()
		for i in exmc:
			sn=i[0]
			cn=i[1]
		print("Check1")
		k=0
		print(sn,dat,typ,cn,k,lat,lon)
		#query1 = "INSERT INTO schools VALUES (:center, :schoolname, :contactNO, :	email)"
		#cur.execute(query1,{'center':c, 'schoolname':name,'contactNO':cn,'email':email})
		cur.execute("""INSERT INTO exams (school_name,dat,type,cn,over,lat,long) VALUES (?,?,?,?,?,?,?);""",(sn,dat,typ,cn,k,lat,lon))
		
		print("hello")
		conn.commit()
		conn.close()
		return render(request, 'slog/wshow.html', { })
		
	except:
		return render(request, 'slog/logschool.html', { })
def vbooked(request):
	conn = sqlite3.connect('/home/suraj/Documents/website/schools.db')
	cur = conn.cursor()
	print("Check1")
	#zones = cur.execute(query1)
	if sid is None:
		return render(request, 'slog/logschool.html', { })
	tablename="s"+str(sid)
	print(tablename	)
	#query1 = "INSERT INTO schools VALUES (:center, :schoolname, :contactNO, :	email)"y
	b = cur.execute("""select ID,email,type,cn from """+tablename+""";""")
	print(b)
	return render(request, 'slog/vbooked.html', {"tabless1":b})
	conn.commit()
	conn.close()
		
def delt(request):
	
	return render(request, 'Home/post_list.html', { })


def get10(request):

	try:
		conn = sqlite3.connect('schools.db')
		cur = conn.cursor()
		print("Check1")
		if sid is None:
			return render(request, 'slog/logschool.html', {})
    		#zones = cur.execute(query1)
		ps = cur.execute("""SELECT * FROM schools WHERE ID="""+ sid +""";""")
		pc = ps.fetchall()
		for i in pc:
			a=i[4]
			b=i[5]
		ps = cur.execute("""SELECT * FROM volunteers;""")
		pc = ps.fetchall()
		latitudes = list()
		longitudes = list()
		names = list()
		emails = list()
		typ = list()
		cns = list()
		ids = list()
		k=0
		for i in pc:
    			latitudes.append(i[5])
    			longitudes.append(i[6])
    			names.append(i[3])
    			emails.append(i[4])
    			typ.append(i[2])
    			cns.append(i[0])
    			ids.append(i[1])
    			k=k+1
		m=int(k)
		eighteen=18.00
		
		for i in range(0,m):
			longitudes[i] = longitudes[i] - 73.00
			latitudes[i] = latitudes[i] - eighteen
			latitudes[i] = latitudes[i] * 1000000
			longitudes[i] = longitudes[i] * 1000000
			print(latitudes[i],longitudes[i])
		df = pd.DataFrame()	
		df['latitude'] = latitudes
		df['longitude'] = longitudes
		df['latitude'] = df['latitude'] - float(a)
		df['longitude'] = df['longitude'] - float(b)
		for i in range(0,k):
			print(df['latitude'][0],df['latitude'][1])
		df['latitude'] =df['latitude']*df['latitude']
		df['longitude'] =df['longitude']*df['longitude']
		for i in range(0,k):
			print(df['latitude'][0],df['latitude'][1])
		sum = pd.Series()
		sum = df['longitude'] + df['latitude'] 
		a=sum.as_matrix()
		l=np.argsort(a)
		x = sum.idxmin()+1
		f=0
		table_data1 = list()
		table_data2 = list()
		table_data3 = list()
		table_data4 = list()
		table_data5 = list()
		table_data = list()
		for i in l:
			table_data1.append(names[i])
			table_data2.append(cns[i])
			table_data3.append(typ[i])
			table_data4.append(ids[i])
			table_data5.append(emails[i])
			f=f+1
		table_data.append(table_data1)
		table_data.append(table_data2)
		table_data.append(table_data3)
		table_data.append(table_data4)
		table_data.append(table_data5)
		z=np.array(table_data)
		b=np.transpose(z)
		return render(request, 'slog/get10.html', {"tabless1":b})
		conn.commit()
		conn.close()
	except:
		return render(request, 'slog/logschool.html', { })
