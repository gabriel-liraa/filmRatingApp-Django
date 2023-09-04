from django.urls import path
from filmRating.views.RatingViews import (
    add_rating_view,
    remove_rating_view,
    rated_films_view,
)

urlpatterns = [
    path("add-rating/<int:film_id>/", add_rating_view, name="add-rating"),
    path("remove-rating/<int:film_id>", remove_rating_view, name="remove-rating"),
    path("rated_films/", rated_films_view, name="rated-films"),
]
