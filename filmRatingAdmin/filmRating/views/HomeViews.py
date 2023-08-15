from django.shortcuts import render
from django.core.paginator import Paginator
from filmRating.models.Film import Film


def home(request):
    search = request.GET.get("search")
    films = Film.objects

    if search is not None and search != "":
        films = Film.objects.filter(name__icontains=search)

    films = films.all().order_by("name")

    get_copy = request.GET.copy()
    parameters = get_copy.pop("page", True) and get_copy.urlencode()

    if len(films) > 0:
        paginator = Paginator(films, 3)
        page_number = request.GET.get("page")
        films = paginator.get_page(page_number)

    context = {
        "films": films,
        "parameters": parameters,
    }

    print(parameters)

    return render(request, "home/home.html", context=context, status=200)
