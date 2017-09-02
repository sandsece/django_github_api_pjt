from django.shortcuts import render , HttpResponse

# Create your views here.

#URLs map to functions in your views.py which in turn will pass data to a template. 

def index(request):
    return HttpResponse('Hello World!')
    
def test(request):
    return HttpResponse('Second view=>test!')
    