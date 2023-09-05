from filmRating.models.Profile import Profile
from django.contrib.auth.decorators import login_required
from filmRating.models.Film import Film
from django.core.paginator import Paginator
from django.shortcuts import render, redirect


@login_required
def favorites_view(request):
    try:
        profile = Profile.objects.filter(user=request.user)[0]
        films = profile.favorites.all()

        if len(films) > 0:
            paginator = Paginator(films, 3)
            page = request.GET.get("page") or 1
            films = paginator.get_page(page)

        context = {
            "films": films,
        }

        return render(request, "favorites/favorites.html", context=context, status=200)

    except:
        msg = "Impossível acessar os filmes favoritos."
        _type = "danger"

        return redirect(f"/?msg={msg}&type={_type}")


@login_required
def add_favorite_view(request, id):
    post_copy = f"{request.POST.get('path')}"
    post_copy += f"?page={request.POST.get('page')}"
    post_copy += f"&search={request.POST.get('search')}"
    try:
        profile = Profile.objects.filter(user=request.user)[0]
        film = Film.objects.filter(id=id)[0]
        profile.favorites.add(film)
        profile.save()
        msg = "Filme favoritado com sucesso!"
        _type = "success"

    except:
        msg = "Ocorreu um erro ao tentar favoritar o filme."
        _type = "danger"

    post_copy += ("&" if post_copy else "?") + f"msg={msg}&type={_type}"

    return redirect(to=f"{post_copy}", status=200)


@login_required
def remove_favorite_view(request, id):
    post_copy = f"{request.POST.get('path')}"
    post_copy += f"?page={request.POST.get('page')}"
    post_copy += f"&search={request.POST.get('search')}"
    try:
        profile = Profile.objects.filter(user=request.user)[0]
        film = Film.objects.filter(id=id)[0]
        profile.favorites.remove(film)
        profile.save()
        msg = "Filme removido dos favoritos!"
        _type = "success"

    except:
        msg = "Ocorreu um erro ao tentar remover o filme dos favoritos."
        _type = "danger"

    post_copy += ("&" if post_copy else "?") + f"msg={msg}&type={_type}"

    return redirect(to=f"{post_copy}", status=200)
