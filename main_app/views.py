from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def home (request):
    return HttpResponse ('working so far')

def about (request):
    return HttpResponse('<h1> This is the About page </h1>')
