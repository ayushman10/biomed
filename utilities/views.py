from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Django ready to receive data')

def processed(request):
    return HttpResponse('we are at processed function')

    
    

   