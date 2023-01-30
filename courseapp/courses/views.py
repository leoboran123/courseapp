from datetime import date
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse

data = {
    "programlama":"Programlama kategorisindeki kurslar",
    "mobil":"Mobil programlama kategorisindeki kurslar",
    "web":"Web programlama kategorisindeki kurslar"
}

db = {
    "courses":[
        {
        "title":"Javascript Kursu",
        "description": "Javascript kurs açıklaması",
        "imageUrl":"https://i.ytimg.com/vi/jS4aFq5-91M/maxresdefault.jpg",
        "slug":"javascript",
        "date":date(2022,10,10),
        "isActive":True,
        "isUpdated":True
        },
        {
        "title":"Python Kursu",
        "description": "Python kurs açıklaması",
        "imageUrl":"https://www.upf.edu/documents/222910037/261564223/python2/7b73d5da-bcc5-72e0-db72-f1e763612931?t=1665491363773",
        "slug":"python",
        "date":date(2022,9,10),
        "isActive":True,
        "isUpdated":False
        },
        {
        "title":"web geliştirme Kursu",
        "description": "web geliştirme kurs açıklaması",
        "imageUrl":"https://www.kodsihirbazi.com/wp-content/uploads/2018/03/Web-Geli%C5%9Ftirme-501x330.png",
        "slug":"web-geliştirme",
        "date":date(2022,8,10),
        "isActive":True,
        "isUpdated":True
        }
    ],
    "categories": [
            {"id":1, "name":"Programlama","slug":"programlama"},
            {"id":2, "name":"Mobil Uygulama","slug":"mobil"},
            {"id":3, "name":"Web Geliştirme","slug":"web"},
        
        ]
}



def index(req):
    kurslar = db["courses"]
    kategoriler = db["categories"]

    return render(req,"courses/index.html", {
        'categories':kategoriler,
        'courses':kurslar
    })

    
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


