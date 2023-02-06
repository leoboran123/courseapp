from datetime import date
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse
from .models import Course,Categorie
from django.core.paginator import Paginator



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
    kurslar = Course.objects.filter(categories__slug=slug, isActive=True).order_by("date")
    kategoriler = Categorie.objects.all()

    paginator = Paginator(kurslar, 2)
    page = req.GET.get('page',1)
    courses = paginator.get_page(page)

    numberofPages = []

    i=0
    while i<paginator.num_pages:
        i+=1
        numberofPages.append(i)

    return render(req, 'courses/index.html', {
        'categories':kategoriler,
        'courses':courses,
        'seciliKategori': slug,
        'paginator': paginator,
        'nop':numberofPages,
        'page':int(page)
        
        
    })




