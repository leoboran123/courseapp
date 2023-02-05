from datetime import date
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse
from .models import Course,Categorie



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
        "imageUrl":"1.jpg",
        "slug":"javascript",
        "date":date(2022,10,10),
        "isActive":True,
        "isUpdated":True
        },
        {
        "title":"Python Kursu",
        "description": "Python kurs açıklaması",
        "imageUrl":"2.png",
        "slug":"python",
        "date":date(2022,9,10),
        "isActive":True,
        "isUpdated":False
        },
        {
        "title":"web geliştirme Kursu",
        "description": "web geliştirme kurs açıklaması",
        "imageUrl":"3.png",
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
    kurslar = Course.objects.filter(isActive=1)
    kategoriler = Categorie.objects.all()

    return render(req,"courses/index.html", {
        'categories':kategoriler,
        'courses':kurslar
    })

    
def details(req, course_id):
    try:
        course = Course.objects.get(slug=course_id)  
    except:
        raise Http404()

    # --------------öbür yol---------------

    # course = get_object_or_404(Course, pk=kurs_id)

    return render(req, 'courses/details.html', {
            'course': course
        })



def getCoursesByCategory(req, slug):
    kurslar = Course.objects.filter(categorie__slug=slug, isActive=True)
    kategoriler = Categorie.objects.all()

    return render(req, 'courses/index.html', {
        'categories':kategoriler,
        'courses':kurslar,
        'seciliKategori': slug
    })




