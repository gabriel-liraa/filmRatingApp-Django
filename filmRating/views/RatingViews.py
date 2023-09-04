from filmRating.forms.RatingForm import RatingForm
from filmRating.models import Film, Rating
from django.shortcuts import render, redirect
from django.core.paginator import Paginator


def add_rating_view(request, film_id):
    if not request.user.is_authenticated:
        return redirect(to="/user/login")
    message = None
    film_rated = Film.objects.filter(id=film_id).first()
    rating = Rating.objects.filter(film_rated=film_rated, user=request.user).first()
    initial = {
        "user": request.user,
        "film_rated": film_rated,
    }
    if request.method == "POST":
        forms = RatingForm(request.POST, instance=rating, initial=initial)

    else:
        forms = RatingForm(instance=rating, initial=initial)

    if forms.is_valid():
        forms.save()
        message = {
            "type": "success",
            "msg": "Avaliação foi salva com sucesso!",
        }

    else:
        if request.method == "POST":
            message = {
                "type": "danger",
                "msg": "Erro ao salvar a avaliação.",
            }

    context = {
        "forms": forms,
        "message": message,
        "film_rated": film_rated,
    }

    return render(request, "ratings/ratings.html", context=context, status=200)


def remove_rating_view(request, film_id):
    rating = Rating.objects.filter(film_rated__id=film_id).first()
    try:
        rating.delete()
        msg = "Avaliação removida com sucesso!"
        _type = "success"

    except:
        msg = "Erro ao deletar avaliação."
        _type = "danger"

    return redirect(f"/rating/rated_films/?msg={msg}&type={_type}")


def rated_films_view(request):
    ratings = Rating.objects.filter(user=request.user).order_by("-created_at").all()
    if len(ratings) > 0:
        paginator = Paginator(ratings, 4)
        page = request.GET.get("page")
        ratings = paginator.get_page(page)

    context = {
        "ratings": ratings,
    }
    return render(request, "ratings/rated_films.html", context=context, status=200)
