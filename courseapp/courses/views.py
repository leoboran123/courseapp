from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    return HttpResponse('<h1>anasayfa</h1>')

def kurslar(req):
    return HttpResponse('kurs listesi')


# Create your views here.
