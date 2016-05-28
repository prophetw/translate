from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello world')

def home(request):
    string = '好像附参考大家今晚大家啊'
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    # return render(request, 'home.html', {'string': string})
    return render(request, 'home.html', {'TutorialList': TutorialList })
