from filmRating.models.Profile import Profile
from filmRating.models.Film import Film
from django.http import HttpResponse
from django.shortcuts import render


def profile_view(request):
    try:
        id = request.POST.get("id")
        profile = Profile.objects.filter(user__id=id)[0]
        films = Film.objects.filter(owner__id=id).all()
        context = {
            "profile": profile,
            "films": films,
        }

        return render(request, "profile/profile.html", context=context, status=200)

    except:
        return HttpResponse("Erro")
