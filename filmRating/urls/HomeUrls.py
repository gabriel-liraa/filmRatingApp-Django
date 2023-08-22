from django.urls import path
from filmRating.views.HomeViews import home, add_favorite_view

urlpatterns = [
    path("", home, name="home"),
    path("favorite/<int:id>", add_favorite_view, name="add-favorite"),
]
