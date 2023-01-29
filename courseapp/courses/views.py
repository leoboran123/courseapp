from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse

data = {
    "programlama":"Programlama kategorisindeki kurslar",
    "mobil":"Mobil programlama kategorisindeki kurslar",
    "web":"Web programlama kategorisindeki kurslar"
}

def kurslar(req):
    return HttpResponse('kurs detay sayfası')
    
def details(req, kurs_adi):
    return HttpResponse(kurs_adi)

def getCoursesByCategory(req, category_name):
    # category değişkeni url üzerine girilen değerdir.
    text=""
    try:
        text=data[category_name]
        return HttpResponse(text)
    except:
        return HttpResponse("Yanlış kategori seçimi!")


    
def getCoursesByCategoryId(req, category_id):
    category_list = list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponse("Yanlış kategori seçimi!")

    category = category_list[category_id - 1]

    redirect_url= reverse('courses_by_category', args=[category])

    return redirect(redirect_url)


