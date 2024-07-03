from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World')

def index_message(request):
    return HttpResponse('<h1>test message</h1>')