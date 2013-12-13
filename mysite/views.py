from django.shortcuts import render
#from django.template.loader import get_template
#from django.template import Context
from django.http import HttpResponse, Http404
import datetime

def hello(request):
    return HttpResponse("Hello world")

def my_homepage_view(request):
	title = "This is my Home Page"
	return render(request, 'mypage_template.html', {'title': title})
	

def current_datetime(request):
	now = datetime.datetime.now()
	
	# Because we do the follow 3 lines of code so often, there is a render() shortcut
	# 	render(request, 'template.html', {'variable': value, 'variable2': value2, ...})
	'''
	The first argument to render() is the request, 
	the second is the name of the template to use. 
	The third argument, if given, should be a dictionary 
	to use in creating a Context for that template. 
	If you dont provide a third argument, 
	render() will use an empty dictionary.
	'''
	#		t = get_template('time_template.html')
	#		html = t.render(Context({'current_date': now}))
	#		return HttpResponse(html)
	return render(request, 'time_template.html', {'current_date': now})

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()

	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	
	return render(request, 'hours_ahead_template.html', {'hour_offset': offset,
		'next_time': dt})

def logged_in(request):
	html = "<html><body><h1>You are currently logged in!</h1></body></html>"
	return HttpResponse(html)