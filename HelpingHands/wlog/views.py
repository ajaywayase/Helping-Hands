# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sqlite3
from django.shortcuts import render
import numpy as np
import pandas as pd
from django.core.mail import EmailMessage
from django.core.mail import send_mail
# Create your views here.

def logwriter(request):
    
    return render(request, 'wlog/logwriter.html', {})

def sshow(request):
	try:
		global c,lat,lon
		c = request.POST.get('wid')
		y = request.POST.get('lat')
		y1 = request.POST.get('long')
		print(c)
		if y=='':
			return render(request, 'wlog/logwriter.html', {})
		if y is None:
			return render(request, 'wlog/logwriter.html', {})
		conn = sqlite3.connect('/home/suraj/Documents/website/schools.db')
		cur = conn.cursor()
		cur.execute("""insert into current (id,lat,lon) VALUES (?,?,?)""",(c,y,y1))
		conn.commit()
		query1 = "Select * from current;"		#returns tuple of lat and long
		print(query1)
		ps = cur.execute(query1)
		pc = ps.fetchall()
		for i in pc:
			c=i[0]
			a=i[1]
			b=i[2]
		a=float((float(a)-18.00)*1000000)
		b=float((float(b)-73.00)*1000000)
	
	
	
		query1 = "Select * from exams where over=0;"		#returns tuple of lat and long
		print(query1)
		ps = cur.execute(query1)
		pc = ps.fetchall()
		
		latitudes = list()
		longitudes = list()
		names = list()
		dates = list()
		typ = list()
		cns = list()
		ids = list()
		k=0
		for i in pc:
			latitudes.append(i[5])
			longitudes.append(i[6])
			names.append(i[0])
			dates.append(i[1])
			typ.append(i[2])
			cns.append(i[3])
			ids.append(i[7])
			k=k+1
			m=int(k)
			eighteen=18.00
		for i in range(0,m):
			if latitudes[i] is None:
				latitudes[i] = 18.122332
			latitudes[i] = latitudes[i] - 18.00
			if longitudes[i] is None:
				longitudes[i] = 71.263737
			longitudes[i] = longitudes[i] - 71.00
			latitudes[i] = latitudes[i] * 1000000
			longitudes[i] = longitudes[i] * 1000000
			#latitudes[i] = latitudes[i] - float(a)
			#longitudes[i] = longitudes[i] - float(b)
			print(latitudes[i],longitudes[i])
		#for i in range(0,k):
			#print(latitudes[i],longitudes[i])
		#print(latitudes[0])
		df = pd.DataFrame()
		df['latitude'] = latitudes
		df['longitude'] = longitudes		
		#df['latitude'] = df['latitude'] - 18.00
		#df['longitude'] = df['longitude'] - 73.00
		#df['latitude'] = df['latitude']*1000000
		#df['longitude'] = df['longitude']*1000000
		print(a,b)
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
		#x = sum.idxmin()+1
		#for i in sum:
			#print(i)
		print("hello")
		f=0
		table_data1 = list()
		table_data2 = list()
		table_data3 = list()
		table_data4 = list()
		table_data = list()
		tab_data = list()
		table_data7 = list()
		table_data8 = list()
		table_data9 = list()
		#table_dat = [f][4]
		for i in l:
			tab_data.append(ids[i])
			table_data1.append(names[i])
			table_data2.append(dates[i])
			table_data3.append(typ[i])
			table_data4.append(cns[i])
			f=f+1
		#table_dat = [f][4]
		table_data.append(tab_data)
		table_data.append(table_data1)
		table_data.append(table_data2)
		table_data.append(table_data3)
		table_data.append(table_data4)
		z=np.array(table_data)
		b=np.transpose(z)
		#table_dat.append(table_data6)
		#table_dat.append(table_data7)
		#table_dat.append(table_data8)
		#table_dat.append(table_data9)
		print("hello2")
		query2 = """Select ID,school_name,dat,type,cn from exams where over=0 ORDER BY dat;"""		#returns tuple of lat and long
		print(query2)
		sp = cur.execute(query2)
		t = sp.fetchall()
		query3 = "Select ID,school_name,dat,type,cn from exams where over=0 ORDER BY school_name;"		#returns tuple of lat and long
		print(query3)
		sp2 = cur.execute(query3)
		nt = sp2.fetchall()
		print("hello3")
		
		return render(request, 'wlog/sshow.html', {"tabless1":b,"tabless2":t,"tabless3":nt})
		print("hello")
		conn.commit()
		conn.close()
	except:
		
		cur.execute("""DELETE FROM current""")
		conn.commit()
		conn.close()
		return render(request, 'wlog/logwriter.html', { })
def userbooked(request):
	try:		
		#c = request.POST.get('wid')
		conn = sqlite3.connect('schools.db')
		cur = conn.cursor()
		query1 = "Select * from current;"		#returns tuple of lat and long
		print(query1)
		ps = cur.execute(query1)
		pc = ps.fetchall()
		for i in pc:
			c=i[0]
		
		tablename="v"+str(c)
		table_data = cur.execute("select ID,name,dat,cn,email,type from """+tablename+""";""")
		return render(request, 'wlog/userbooked.html', {"tabless1":table_data})
		conn.commit()
		conn.close()
	except:
		conn = sqlite3.connect('schools.db')
		cur = conn.cursor()
		cur.execute("""DELETE FROM current""")
		conn.commit()
		conn.close()
		return render(request, 'wlog/logwriter.html', {})
		
	    
def book(request):
	   
	return render(request, 'wlog/book.html', { })
	    
def book1(request):

	eid=request.POST.get("eid")
	c=request.POST.get("wid")
	conn = sqlite3.connect('schools.db')
	cur = conn.cursor()
	
	print(eid)
	query=("""SELECT * FROM exams WHERE ID="""+ str(eid) +""";""")
	exms=cur.execute(query)
	exmc = exms.fetchall()
	for i in exmc:
		edat=i[1]
		etyp=i[2]
		sn=i[0]
		eid=i[7]
		scn=i[3]
	print(sn)
	if c is None:
		return render(request, 'wlog/logwriter.html', {})
	exm=cur.execute("""SELECT * FROM volunteers WHERE ID="""+ str(c) +""";""")
	exc = exm.fetchall()
	for i in exc:
	    	vemail=i[4]
	    	vcn=i[0]
	    	vtype=i[2]
	    	vname=i[3]	
	sn2="\""+sn+"\""
	kp=1
	query3="""UPDATE exams SET over = """+ str(kp) +""" where ID = """+ str(eid) +""";"""
	print(query3)
	cur.execute(query3)
	query4="""SELECT * FROM schools WHERE schools.sn= """+ sn2 +""";"""
	ms=cur.execute(query4)
	print(query4)
	exmc = exms.fetchall()
	id=102
	for i in exmc:
	   		sid=i[3]
	tablename="s"+str(sid)
	print(tablename,c,vname,vtype,vcn,vemail)
	cur.execute("""INSERT INTO s115 (ID,sn,type,cn,email) VALUES (?,?,?,?,?)""",(c,vname,vtype,vcn,vemail))
	conn.commit()
	tablename="v"+str(c)
	dfg="abc@gmaill.com"
	print(tablename)
	cur.execute("""INSERT INTO """+tablename+""" (ID,name,dat,cn,email,type) VALUES (?,?,?,?,?,?);""",(eid,sn,edat,scn,dfg,etyp))
	conn.commit()
	conn.close()
	to_email = 'ajaywayase98@gmail.com'
	s="Your EXAM ID is "+str(eid)
	email = EmailMessage("Exam booked SUCCESSFULLY!", s,'ajaywayase2016@gmail.com' ,['ajaywayase98@gmail.com'])
	email.send()
	send_mail('Subject here','Here is the message.','ajaywayase2016@gmail.com',['ajaywayase98@gmail.com'],fail_silently=False,)
	return render(request, 'Home/post_list.html', { })
def delt(request):
	try:
		conn = sqlite3.connect('schools.db')
		cur = conn.cursor()
		cur.execute("""DELETE FROM current""")
		conn.commit()
		conn.close()
		return render(request, 'Home/post_list.html', { })
	except:
		return render(request, 'Home/post_list.html', {})	
		





	

