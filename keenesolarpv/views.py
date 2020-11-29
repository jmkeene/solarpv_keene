from django.shortcuts import render
from django.http import HttpResponse


def Project1(request):
	return render(request, 'keenesolarpv/Project1.html')

def registration(request):
	return render(request, 'keenesolarpv/registration.html')

def login(request):
	return render(request, 'keenesolarpv/login.html')

def news(request):
	return render(request, 'keenesolarpv/news.html')

def ourtech(request):
	return render(request, 'keenesolarpv/ourtech.html')

def web_portal(request):
	return render(request, 'keenesolarpv/web_portal.html')

def testing(request):
	return render(request, 'keenesolarpv/testing.html')

