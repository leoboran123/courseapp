from django.urls import path
from django.http import HttpResponse
from . import views
# http://127.0.0.1:8000/ - anasayfa
# http://127.0.0.1:8000/home - anasayfa
# http://127.0.0.1:8000/kurslar - kurs listesi

# <> arası dinamiktir. oraya yazılan değer views.py dosyasındaki 
# getCoursesByCategory isimli fonksiyona gönderilir.

urlpatterns = [
    path('login',views.user_login, name="user_login"),
    path('register',views.user_register, name="user_register"),
    path('change-password',views.change_password, name="change_password"),
    path('logout',views.user_logout, name="user_logout"),

    
]
