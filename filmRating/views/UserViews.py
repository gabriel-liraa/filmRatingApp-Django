from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from filmRating.forms.UserForms import UserLoginForm, UserRegisterForm


def login_view(request):
    if request.method == "POST":
        user_login = authenticate(
            username=request.POST.get("username"), password=request.POST.get("password")
        )
        if user_login is not None:
            login(request, user_login)
            return redirect(to="home")
        else:
            msg = "Erro ao fazer login."
            _type = "danger"
            return redirect(to=f"/?msg={msg}&type={_type}")

    else:
        forms = UserLoginForm()
        context = {
            "forms": forms,
        }
        return render(request, "user/login.html", context=context, status=200)


def logout_view(request):
    logout(request)
    return redirect(to="home")


def register_user_view(request):
    forms = UserRegisterForm()
    context = {
        "forms": forms,
    }

    return render(request, "user/register.html", context=context, status=200)
