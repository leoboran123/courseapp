from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 


def user_login(req):
    if req.user.is_authenticated:
        return redirect("kurslar")

    if req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]

        user = authenticate(req, username=username, password=password)
        
        if user is not None:
            login(req, user)
            nextUrl = req.GET.get('next', None)

            if nextUrl is None:
                return redirect("kurslar")
            else:
                return redirect(nextUrl)
        else:
            return render(req, "account/login.html", {
                "error":"Kullanıcı adı ya da parola yanlış"
            })

    else:
        return render(req, 'account/login.html')



def user_register(req):
    if req.method == "POST":
        username = req.POST["username"]
        email = req.POST["email"]
        password = req.POST["password"]
        repassword = req.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username = username).exists():
                return render(req, 'account/register.html', {
                "error":"Bu kullanıcı adı kullanılıyor!",
                "username":username,
                "email":email
                })
            else:
                if User.objects.filter(email = email).exists():
                    return render(req, 'account/register.html', {
                    "error":"Bu email kullanılıyor!",
                    "username":username,
                    "email":email
                    })
                else:
                    user = User.objects.create_user(username = username, email = email, password = password)
                    user.save()
                    return redirect("user_login")

        else:
            return render(req, 'account/register.html', {
                "error":"Girilen parolalar eşleşmiyor!",
                "username":username,
                "email":email
            })
            
    else:
        return render(req, 'account/register.html')


def user_logout(req):
    logout(req)
    return redirect("kurslar")




