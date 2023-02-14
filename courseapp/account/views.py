from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.contrib import messages
from account.forms import loginUserForm


def user_login(req):
    if req.user.is_authenticated:
        return redirect("kurslar")

    if req.method == "POST":
        form = loginUserForm(req, data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(req, username=username, password=password)
        
            if user is not None:
                login(req, user)
                messages.add_message(req ,messages.SUCCESS, "Giriş başarılı!")
                nextUrl = req.GET.get('next', None)

                if nextUrl is None:
                    return redirect("kurslar")
                else:
                    return redirect(nextUrl)
            else:
                return render(req, "account/login.html", {
                    "form":form
                })
        else:
            return render(req, "account/login.html", {
                "form":form
            })

    else:
        form = loginUserForm(req)

        return render(req, 'account/login.html', {
            "form":form
        })



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
    messages.add_message(req ,messages.SUCCESS, "Çıkış başarılı!")
    logout(req)
    return redirect("kurslar")




