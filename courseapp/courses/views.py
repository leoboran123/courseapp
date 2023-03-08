from datetime import date
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse

from courses.forms import CourseCreateForm, CourseEditForm, uploadForm
from .models import Course,Categorie, uploadModel, Slider
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required, user_passes_test

import random
import os


def index(req):
    kurslar = Course.objects.filter(isActive=1, isHome=1)
    kategoriler = Categorie.objects.all()
    sliders = Slider.objects.filter(is_active=True)


    return render(req,"courses/index.html", {
        'categories':kategoriler,
        'courses':kurslar,
        'sliders':sliders,
    })


def isAdmin(user):
    return user.is_superuser


@user_passes_test(isAdmin)
def create_course(req):

    if req.method=="POST":
        form = CourseCreateForm(req.POST, req.FILES)

        if form.is_valid():
            form.save()
            return redirect("/kurslar")

        else:
            pass

    else:
        form = CourseCreateForm()
        
    return render(req, "courses/create-course.html", {
        "form":form
    })


@user_passes_test(isAdmin)
def course_list(req):
    kurslar = Course.objects.all()

    return render(req,"courses/course-list.html", {
        'courses':kurslar
    })


@login_required()
def course_edit(req,id):
    course = get_object_or_404(Course, pk=id)

    if req.method=="POST":
        form = CourseEditForm(req.POST, req.FILES, instance=course)
        form.save()
        return redirect("course_list")
    else:
        form = CourseEditForm(instance=course)

    return render(req, "courses/edit-course.html", {
        "form":form
    })

def course_delete(req,id):
    course = get_object_or_404(Course, pk=id)

    if req.method == "POST":
        course.delete()
        return redirect("course_list")
    


    return render(req, "courses/course-delete.html", {
        "course":course
    })

def upload(req):
    if req.method == "POST":
        form = uploadForm(req.POST, req.FILES)

        if form.is_valid():
            model = uploadModel(image=req.FILES["image"])
            model.save()
            return render(req,"courses/success.html")

    else:    
        form = uploadForm()


    return render(req, "courses/upload.html",{
        "form":form
    })



def search(req):
    if "q" in req.GET and req.GET["q"] != "":
        q = req.GET["q"]
        kurslar = Course.objects.filter(isActive=True, title__contains=q).order_by("date")
        kategoriler = Categorie.objects.all()
    else:
        return redirect("/kurslar")


    return render(req, 'courses/search.html', {
        'categories':kategoriler,
        'courses':kurslar,
  
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

    return render(req, 'courses/list.html', {
        'categories':kategoriler,
        'courses':courses,
        'seciliKategori': slug,
        'paginator': paginator,
        'nop':numberofPages,
        'page':int(page)
        
        
    })




