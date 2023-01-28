from django.urls import path
from django.http import HttpResponse
from . import views
# http://127.0.0.1:8000/ - anasayfa
# http://127.0.0.1:8000/home - anasayfa
# http://127.0.0.1:8000/kurslar - kurs listesi

# <> arası dinamiktir. oraya yazılan değer views.py dosyasındaki 
# getCoursesByCategory isimli fonksiyona gönderilir.

urlpatterns = [
    path('',views.kurslar),
    path('list',views.kurslar),
    path('details',views.details),
    path('<category>',views.getCoursesByCategory),


]
