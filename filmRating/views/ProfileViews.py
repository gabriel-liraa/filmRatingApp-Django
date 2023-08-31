from filmRating.models.Profile import Profile
from filmRating.models.Film import Film
from filmRating.forms.UserProfileForm import UserProfileForm, UserForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User


def profile_view(request, id):
    try:
        profile = Profile.objects.filter(user__id=id)[0]
        created_films = Film.objects.filter(owner__id=id).all()

        if len(created_films) > 0:
            paginator = Paginator(created_films, 2)
            page = request.GET.get("page")
            created_films = paginator.get_page(page)

        context = {
            "profile": profile,
            "created_films": created_films,
        }

        return render(request, "profile/profile.html", context=context, status=200)

    except:
        msg = "Impossível acessar perfil."
        _type = "danger"
        parameters = f"?msg={msg}&type={_type}"
        return redirect(to=f"/{parameters}", status=200)


def edit_profile(request):
    emailUnused = True
    message = None
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == "POST":
        profileForm = UserProfileForm(
            data=request.POST, files=request.FILES, instance=profile
        )
        userForm = UserForm(data=request.POST, instance=request.user)
        verifyEmail = (
            Profile.objects.filter(user__email=request.POST.get("email"))
            .exclude(user__id=request.user.id)
            .first()
        )
        emailUnused = verifyEmail is None

    else:
        profileForm = UserProfileForm(instance=profile)
        userForm = UserForm(instance=request.user)

    if profileForm.is_valid() and userForm.is_valid() and emailUnused:
        profileForm.save()
        userForm.save()
        message = {"type": "success", "msg": "Dados atualizados com sucesso!"}

    else:
        if request.method == "POST":
            if emailUnused:
                message = {"type": "danger", "msg": "Dados inválidos."}

            else:
                message = {"type": "warning", "msg": "Email já cadastrado."}

    context = {
        "profileForm": profileForm,
        "userForm": userForm,
        "message": message,
    }

    return render(request, "profile/edit_profile.html", context=context, status=200)
