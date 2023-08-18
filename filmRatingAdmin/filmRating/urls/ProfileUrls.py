from django.urls import path
from filmRating.views.ProfileViews import profile_view

urlpatterns = [
    path("", profile_view, name="profile"),
]
