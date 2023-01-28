from django.shortcuts import render
from django.http import HttpResponse


def kurslar(req):
    return HttpResponse('kurs listesi')


def details(req):
    return HttpResponse('kurs detay sayfası')

def getCoursesByCategory(req, category):
    # category değişkeni url üzerine girilen değerdir.
    text=""
    if(category=="programlama"):
        text = "Programlama kategorisindeki kategoriler"
    elif(category=="mobil-programlama"):
        text = "Mobil programlama kategorisindeki kategoriler"
    else:
        text = "Yanlış bir kategori seçtiniz"
    
    return HttpResponse(text)
    

# Create your views here.
