from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from filmRating.models.Film import Film
from filmRating.models.Profile import Profile


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

    return render(request, "home/home.html", context=context, status=200)


def add_favorite_view(request, id):
    post_copy = f"?page={request.POST.get('page')}"
    post_copy += f"&search={request.POST.get('search')}"
    if request.user.is_authenticated:
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

    else:
        msg = "É preciso uma conta para favoritar um filme"
        _type = "danger"

    post_copy += ("&" if post_copy else "?") + f"msg={msg}&type={_type}"

    return redirect(to=f"/{post_copy}", status=200)
