# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sqlite3
from django.shortcuts import render
import sqlite3
# Create your views here.

def regschool(request):

	
	return render(request, 'sreg/regschool.html', {})


def regschool1(request):
	try:
		global lat,lon
		lat = request.POST.get('lat')
		lon = request.POST.get('long')
		name=request.POST.get('schoolname')
		cn = request.POST.get('contact')
		ID= request.POST.get('schoolid')
		email = request.POST.get('email')
		conn = sqlite3.connect('schools.db')
		cur = conn.cursor()
		print("Check1")
		cur.execute("""SELECT * FROM schools;""")
		cur.execute("""INSERT INTO schools (sn,cn,email,ID,lat,long) VALUES (?,?,?,?,?,?);""",(name,cn,email,ID,lat,lon))
		tablename="s"+str(ID)
		cur.execute(""" CREATE TABLE """ + tablename + """( ID INTEGER,vn TEXT,type TEXT,cn INTEGER,email TEXT);""")

		current_site = get_current_site(request)
		mail_subject = 'Activate your blog account.'
		message = render_to_string('acc_active_email.html', {
		'user': name,
		'domain': current_site.domain,
		'uid':urlsafe_base64_encode(force_bytes(user.pk)),
		'token':account_activation_token.make_token(user),
		})
		to_email = form.cleaned_data.get('email')
		email = EmailMessage(
			mail_subject, message, to=[to_email]
		)
		email.send()
		return HttpResponse('Please confirm your email address to complete the registration')



		conn.commit()
		conn.close()
		return render(request, 'slog/logschool.html', {})
	except:
		return render(request, 'sreg/regschool.html', {})		

