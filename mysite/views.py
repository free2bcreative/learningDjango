from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
import datetime

def hello(request):
    return HttpResponse("Hello world")

def my_homepage_view(request):
	title = "This is my Home Page"
	message = "Welcome First Time Users!"
	if "id" in request.COOKIES:
		message = "Welcome Back!"

	t = get_template('mypage_template.html')
	html = t.render(Context({'title': title, 'user_message': message}))
	response = HttpResponse(html)
	response.set_cookie("id", "123456789")
	return response
	
	#return render(request, 'mypage_template.html', {'title': title, 'user_message': message})
	
def another_page(request):
	title = "This is another page"
	message = "No cookies were sent"
	if "id" in request.COOKIES:
		message = "We got a cookie!"

	return render(request, 'mypage_template.html', {'title': title, 'user_message': message})


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