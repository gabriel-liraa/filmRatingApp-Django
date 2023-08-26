from django.urls import path
from filmRating.views.ProfileViews import profile_view, edit_profile

urlpatterns = [
    path("<int:id>/", profile_view, name="profile"),
    path("edit/", edit_profile, name="edit-profile"),
]
