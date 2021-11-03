from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ntrends(request):
    return HttpResponse("Hello world")
def page1(request):
    return render(request,'pag1.html')
def page2(request):
    return render(request,'pag2.html')
def page3(request):
    return render(request,'pag3.html')
