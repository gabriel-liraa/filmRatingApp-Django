from django.urls import path
from filmRating.views.FavoritesViews import favorites_view

urlpatterns = [
    path("", favorites_view, name="favorites"),
]
