from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from filmRating.forms.UserForms import UserLoginForm, UserRegisterForm


def login_view(request):
    if request.method == "POST":
        user_login = authenticate(
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )
        if user_login is not None:
            login(request, user_login)
            _next = request.GET.get("next")
            if _next is not None:
                return redirect(to=f"{_next}")
            return redirect(to="home")
        else:
            msg = f"Combinação de usuário e senha não encontrada."
            _type = "danger"
            return redirect(to=f"/user/login/?msg={msg}&type={_type}")

    else:
        forms = UserLoginForm()
        context = {
            "forms": forms,
            "title": "Login",
            "submit_text": "Entrar",
            "login_bool": True,
        }
        return render(request, "user/auth.html", context=context, status=200)


@login_required
def logout_view(request):
    logout(request)
    return redirect(to="home")


def register_user_view(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            return redirect(to="home")

        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        register_form = UserRegisterForm(request.POST)

        if register_form.is_valid():
            verify_username = User.objects.filter(username=username).first()
            verify_email = User.objects.filter(email=email).first()

            if verify_username is not None:
                msg = "Nome de usuário já existente"
                _type = "danger"
                return redirect(to=f"/user/register/?msg={msg}&type={_type}")

            elif verify_email is not None:
                msg = "Email já existente"
                _type = "danger"
                return redirect(to=f"/user/register/?msg={msg}&type={_type}")

            else:
                try:
                    user = User.objects.create_user(
                        username=username, email=email, password=password
                    )
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()
                    msg = f"Usuário criado com sucesso!"
                    _type = "success"
                    return redirect(to=f"/user/login/?msg={msg}&type={_type}")

                except:
                    msg = "Erro ao criar usuário."
                    _type = "danger"
                    return redirect(to=f"/user/register/?msg={msg}&type={_type}")

        msg = "Erro no form"
        _type = "danger"
        return redirect(to=f"/user/register/?msg={msg}&type={_type}")

    else:
        forms = UserRegisterForm()
        context = {
            "forms": forms,
            "title": "Registrar",
            "submit_text": "Cadastrar",
            "login_bool": False,
        }

        return render(request, "user/auth.html", context=context, status=200)
