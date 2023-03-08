from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User 
from django.contrib import messages
from account.forms import loginUserForm, NewUserForm, UserChangePasswordForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm


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
        form = NewUserForm(req.POST)

        if form.is_valid():
            form.save()


            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            user = authenticate(req, username=username, password=password)
            login(req, user)
            return redirect("index")

        else:
            return render(req, "account/register.html", {
                "form":form
            })

    else:
        form = NewUserForm()
        return render(req, "account/register.html", {
            "form":form
        })


def user_logout(req):
    messages.add_message(req ,messages.SUCCESS, "Çıkış başarılı!")
    logout(req)
    return redirect("kurslar")

def change_password(req):
    if req.method == "POST":
        form= UserChangePasswordForm(req.user, req.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(req, user)
            messages.success(req, "Parola güncellendi.")
            return redirect("index")
        else:
            return render(req, "account/change_password.html", {
                "form":form 
            })

    form = UserChangePasswordForm(req.user) 

    return render(req, "account/change_password.html", {
        "form":form 
    })


