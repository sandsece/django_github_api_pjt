from django.shortcuts import render , HttpResponse
import json, requests

# Create your views here.

#URLs map to functions in your views.py which in turn will pass data to a template. 

def index(request):
    return HttpResponse('Hello World!')
    
def test(request):
    return HttpResponse('Second view=>test!')
    
def profile(request):
    req = requests.get('https://api.github.com/users/DrkSephy')
    content = req.text
    return HttpResponse(content)
    