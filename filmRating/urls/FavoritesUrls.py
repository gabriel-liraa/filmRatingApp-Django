from django.urls import path
from filmRating.views.FavoritesViews import (
    favorites_view,
    add_favorite_view,
    remove_favorite_view,
)

urlpatterns = [
    path("", favorites_view, name="favorites"),
    path("add/<int:id>", add_favorite_view, name="add-favorite"),
    path("remove/<int:id>", remove_favorite_view, name="remove-favorite"),
]
