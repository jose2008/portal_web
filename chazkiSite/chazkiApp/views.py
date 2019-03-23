from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
	a = {'m':3}
	return render_to_response('index.html')