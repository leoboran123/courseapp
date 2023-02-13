from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def user_login(req):
    if req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]

        user = authenticate(req, username=username, password=password)
        
        if user is not None:
            login(req, user)
            return redirect("index")
        else:
            return render(req, "account/login.html", {
                "error":"Kullanıcı adı ya da parola yanlış"
            })

    else:
        return render(req, 'account/login.html')



def user_register(req):
    return render(req, 'account/register.html')

def user_logout(req):
    return redirect("kurslar")




