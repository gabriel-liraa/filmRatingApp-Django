from filmRating.models.Profile import Profile
from django.core.paginator import Paginator
from django.shortcuts import render, redirect


def favorites_view(request):
    if request.user.is_authenticated:
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

            return render(
                request, "favorites/favorites.html", context=context, status=200
            )

        except:
            msg = "Impossível acessar os filmes favoritos."
            _type = "danger"
            return redirect(f"/?msg={msg}&type={_type}")
