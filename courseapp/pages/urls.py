from django.urls import path
from django.http import HttpResponse
from . import views

# http://127.0.0.1:8000/ - anasayfa
# http://127.0.0.1:8000/home - anasayfa
# http://127.0.0.1:8000/kurslar - kurs listesi



urlpatterns = [
    path('',views.index),
    path('index',views.index, name="index"),
    path('contact',views.contact),
    path('about',views.about),

]
