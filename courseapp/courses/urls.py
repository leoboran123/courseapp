from django.urls import path
from django.http import HttpResponse
from . import views
# http://127.0.0.1:8000/ - anasayfa
# http://127.0.0.1:8000/home - anasayfa
# http://127.0.0.1:8000/kurslar - kurs listesi

# <> arası dinamiktir. oraya yazılan değer views.py dosyasındaki 
# getCoursesByCategory isimli fonksiyona gönderilir.

urlpatterns = [
    path('',views.index, name="kurslar"),
    path('search',views.search, name="search"),
    path('create-course',views.create_course, name="create_course"),
    path('course-list', views.course_list, name="course_list"),
    path('course-edit/<int:id>', views.course_edit, name="edit_course"),
    path('course-delete/<int:id>', views.course_delete, name="delete_course"),
    path('upload', views.upload, name="upload_image"),
    path('<slug:course_id>',views.details, name="course_details"),
    path('kategori/<slug:slug>',views.getCoursesByCategory, name="courses_by_category"),
    

]
