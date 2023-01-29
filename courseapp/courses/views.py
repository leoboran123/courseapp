from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse

data = {
    "programlama":"Programlama kategorisindeki kurslar",
    "mobil":"Mobil programlama kategorisindeki kurslar",
    "web":"Web programlama kategorisindeki kurslar"
}

def index(req):
    return render(req,"courses/index.html")

def kurslar(req):
    list_items=""
    category_list = list(data.keys())

    for category in category_list:
        redirect_url= reverse('courses_by_category', args=[category])
        list_items += f"<li><a href='{redirect_url}'>{category}</a></li>"

    html = f"<h1>Kurs listesi</h1><br><ul>{list_items}</ul>"

    return HttpResponse(html)
    
def details(req, kurs_adi):
    return HttpResponse(kurs_adi)

def getCoursesByCategory(req, category_name):
    # category değişkeni url üzerine girilen değerdir.
    text=""
    try:
        text=data[category_name]
        return render(req, 'courses/courses.html', {
            'category' : category_name,
            'category_text': text
        })
    except:
        return HttpResponse("Yanlış kategori seçimi!")


    
def getCoursesByCategoryId(req, category_id):
    category_list = list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponse("Yanlış kategori seçimi!")

    category = category_list[category_id - 1]

    redirect_url= reverse('courses_by_category', args=[category])

    return redirect(redirect_url)


