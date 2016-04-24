from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse

def index(request):
    return HttpResponse("hello world,you are at the polls index")