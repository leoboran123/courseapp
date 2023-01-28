from django.shortcuts import render
from django.http import HttpResponse




def kurslar(req):
    return HttpResponse('kurs detay sayfası')
    
def details(req, kurs_adi):
    return HttpResponse(kurs_adi)

def getCoursesByCategory(req, category_name):
    # category değişkeni url üzerine girilen değerdir.
    text=""
    if(category_name=="programlama"):
        text = "Programlama kategorisindeki kategoriler"
    elif(category_name=="mobil-programlama"):
        text = "Mobil programlama kategorisindeki kategoriler"
    else:
        text = "Yanlış bir kategori seçtiniz"
    
    return HttpResponse(text)
    
def getCoursesByCategoryId(req, category_id):

    return HttpResponse(category_id + ". kurs")

