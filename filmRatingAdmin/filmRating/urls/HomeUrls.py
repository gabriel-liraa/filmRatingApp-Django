from django.urls import path
from filmRating.views.HomeViews import home

urlpatterns = [
    path("", home, name="home"),
]
