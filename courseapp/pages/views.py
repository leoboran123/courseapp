from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    return HttpResponse('<h1>anasayfa</h1>')

def iletisim(req):
    return HttpResponse("iletişim sayfası")

def hakkimizda(req):
    return HttpResponse('Hakkımızda')