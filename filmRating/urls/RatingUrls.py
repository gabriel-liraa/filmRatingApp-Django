from django.urls import path
from filmRating.views.RatingViews import add_rating_view

urlpatterns = [path("<int:film_id>/", add_rating_view, name="rating")]
