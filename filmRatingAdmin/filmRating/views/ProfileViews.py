from filmRating.models.Profile import Profile
from filmRating.models.Film import Film
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render


def profile_view(request, id):
    try:
        profile = Profile.objects.filter(user__id=id)[0]
        films = Film.objects.filter(owner__id=id).all()

        if len(films) > 0:
            paginator = Paginator(films, 2)
            page = request.GET.get("page")
            films = paginator.get_page(page)

        context = {
            "profile": profile,
            "films": films,
        }

        return render(request, "profile/profile.html", context=context, status=200)

    except:
        return HttpResponse("Erro")
