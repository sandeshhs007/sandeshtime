from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def display_msg_time(request):
	data=datetime.datetime.now()
	hour=int(datetime.datetime.now().hour)
	msg='<h1> Hi client Good'
	if hour>12:
		msg=msg+'Morning'
	elif hour>18:
		msg+='<h1>afternoon</h1>'
	elif hour>21:
		msg+='<h1>evening</h1>'
	else:
		msg+='night'
	msg=msg+'</h1><hr>'

	msg=msg+'<h1>The server time is '+ str(data)+'</h1>'
	return HttpResponse(msg)


