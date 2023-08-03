from django.shortcuts import render
from filmRating.models.Film import Film


def home(request):
    search = request.GET.get("search")
    films = Film.objects

    if search is not None and search != "":
        films = Film.objects.filter(name__icontains=search)

    films = films.all()

    context = {
        "films": films,
    }
    return render(request, "home/home.html", context=context)
